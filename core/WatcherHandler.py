import time
import subprocess
from threading import Timer
from watchdog.events import FileSystemEventHandler


def debounce(wait):
    """ Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = Timer(wait, call_it)
            debounced.t.start()
        return debounced
    return decorator


class Handler(FileSystemEventHandler):

    process = None
    files = []

    @staticmethod
    def whitelisted(src):
        whitelist = ('.idea', '.git', '__pycache__')

        for item in whitelist:
            if item in src:
                return True

    def on_modified(self, event):
        file = event.src_path
        if self.whitelisted(file):
            return
        if file not in self.files and not event.is_directory and "~" not in file:
            self.files.append(file)

        self.restart_server()

    @debounce(1)
    def restart_server(self):
        print("Changed files:")
        for file in self.files:
            print("%s" % file)
        self.files = []
        self.process.terminate()
        self.run_command()
        print("[%s]" % time.asctime(), "Restarting server")

    def run_command(self):
        self.process = subprocess.Popen(['python', './run.py'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

