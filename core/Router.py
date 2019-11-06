from routes import routes


def get_fragments(self, path):
    return list(filter(None, path.split('/')))


class Router:

    def __init__(self, request):
        self.path = request.path

    def exists(self):
        return self.path in routes.keys()

    def get_view(self):
        if self.exists():
            return routes[self.path]
        else:
            return False

# class Route:
#     routes = []
#
#     @staticmethod
#     def get(path, controller, method, name = ""):
#         routes.append({
#             ""
#             "path": path,
#             "controller": controller,
#             "method": method,
#             "name": name,
#             "fragments": getFragments(path)
#         })

# try:
#       module = __import__(module_name)
#       Controller = getattr(module, class_name)
#       instance = Controller()
#     except ImportError:
#        # manage import error
