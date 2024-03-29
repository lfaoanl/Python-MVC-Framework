from core.WatcherHandler import Handler
import sys
import time
import logging
from watchdog.observers import Observer

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler()
    event_handler.run_command()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        print("[%s]" % time.asctime(), "Starting watcher")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("[%s]" % time.asctime(), "Watcher stopped")
    finally:
        event_handler.process.terminate()
    observer.join()
