from string import Formatter
import traceback
from core.Config import config
import sys

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
            # TODO change format brackets
            # Suggestion 1: use Formatter class
            # Suggestion 2: Regex replace:          \$\{( (?:[_a-zA-Z]\w*)(?:\.(?:[_a-zA-Z]\w*))?(?:\[(?:"\w+"|\d+)\])? ?(?:\! ?[s|r])? ?(?:\: ?\w+)?) \}
            page = page.format(**data)
            self.request.write_page(self.RESPONSE_CODE, page)
        except KeyError as e:
            raise KeyError("Undefined variable {} in view '{}'".format(e.__str__(), view))
            pass

            # if config['debug']:
            #     page = "<p><strong>%s</strong></p>" % traceback.format_exc()
            #
            #     for line in traceback.format_stack():
            #         page += "<p>%s</p>" % line
            # else:
            #     page = self.error_page(500, True)
            # pass

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
