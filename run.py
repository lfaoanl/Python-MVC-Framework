import time
import socketserver
from core.RequestHandler import Handler

HOST_NAME = '127.0.0.1'
PORT = 3000

with socketserver.TCPServer((HOST_NAME, PORT), Handler) as httpd:
    print("[%s]" % time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("[%s]" % time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT))
        pass
