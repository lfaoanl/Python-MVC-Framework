from http.server import BaseHTTPRequestHandler
from core.Router import Router
from core.View import View
from core.Config import config
import sys
import traceback

class Http:
    pass


class Handler(BaseHTTPRequestHandler):

    RESPONSE_CODE = 200

    def do_GET(self):
        try:
            route = Router(self)

            view = View(self)
            view.parse(route.get_view())
        except Exception as e:
            if config['debug']:
                info = traceback.format_exception(Exception, e, e.__traceback__)
                page = ''
                for line in info:
                    line = str(line)
                    if "File" in line:
                        page += "<p>%s</p>" % line
                    else:
                        page += "<p><strong>%s</strong></p>" % line
                # TODO add breadcrumbs or traceback or whatever you want to call it

                self.write_page(500, page)
            else:
                view = View(self)
                page = view.error_page(500, True)
                self.write_page(500, page)

    def write_page(self, response_code, page):
        self.send_response(response_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode('UTF-8'))