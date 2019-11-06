from http.server import BaseHTTPRequestHandler
from core.Router import Router
from core.View import View


class Http:
    pass


class Handler(BaseHTTPRequestHandler):

    RESPONSE_CODE = 200

    def do_GET(self):
        route = Router(self)

        view = View(self)
        view.parse(route.get_view())
