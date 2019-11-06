from string import Formatter


class View:

    RESPONSE_CODE = 200
    data = {}

    def __init__(self, request):
        self.request = request

    def parse(self, view, data=None):
        page = self.load(view)
        if data is None:
            data = self.data

        try:
            page = page.format(**data)
        except KeyError:
            page = self.error_page(500, True)
            pass

        self.request.send_response(self.RESPONSE_CODE)
        self.request.send_header("Content-type", "text/html")
        self.request.end_headers()
        self.request.wfile.write(page.encode('UTF-8'))

        return True

    def load(self, view):
        if view is False:
            return self.error_page(404)

        try:
            return self.fetch(view)
        except FileNotFoundError:
            return self.error_page(404)

    @staticmethod
    def fetch(view, src=""):
        file = open("src/View{0}/{1}.html".format(src, view), "r")
        view = file.read()
        file.close()
        return view

    def error_page(self, code, formatted=False):
        self.RESPONSE_CODE = code
        self.data = self.get_error_codes(code)
        page = self.fetch("404", "/errors")

        if formatted:
            return page.format(**self.data)
        return page

    def get_error_codes(self, code):
        error = self.request.responses[code]
        return {
            "code": code,
            "title": error[0],
            "message": error[1],
        }
