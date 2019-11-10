import time
import socketserver
from core.Config import config
from core.RequestHandler import Handler

HOST_NAME = config['server']['host']
PORT = config['server']['port']

with socketserver.TCPServer((HOST_NAME, PORT), Handler) as httpd:
    print("[%s]" % time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("[%s]" % time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT))
        pass
