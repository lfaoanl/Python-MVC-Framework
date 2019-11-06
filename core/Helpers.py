def isSame(a, b):
    return a == b

def find(key, needle, haystack, callback = isSame):
    for object in haystack:
        if callback(object[key], needle):
            return object

# print(find("name", "users", routes))

# def sameRoute(path, route = "/users/edit/31"):
