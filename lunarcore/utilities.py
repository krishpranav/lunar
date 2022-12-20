import asyncio
import inspect
import os

def find_files(path: str, ext: str) -> list:
        foundFiles = []
        for root, _dirs, files in os.walk(path, topdown=False):
            for name in files:
                if name.endswith(ext):
                    filepath = os.path.join(root, name)
                    foundFiles.append(filepath)
        return foundFiles

def print_request(request):
    print(type(request._scope))
    d = dict(request._scope)
    print(d)
    d.pop("headers")
    print(d)
    fields = [
        "path",
        "method",
        "url",
        "headers",
        "query_params",
        "path_params",
        "client",
        "cookies",
        "state",
    ]
    print("*************************************")
    for field in fields:
        try:
            print(field, request[field])
        except:
            print(field, getattr(request, field))
    print(request.url.path, request.url.port, request.url.scheme, dir(request.url))
    for i, j in request.query_params.items():
        print(i, j)
    print("URL related -------")
    for j in [
        "components",
        "fragment",
        "hostname",
        "is_secure",
        "netloc",
        "password",
        "path",
        "port",
        "query",
        "replace",
        "scheme",
        "username",
    ]:
        print(j, getattr(request.url, j))
    for j in getattr(request.url, "components"):
        print(j)
    print("*************************************")


def run_task(task):
    loop = asyncio.get_event_loop()
    loop.create_task(task)


async def create_delayed_task(task, delay, loop):
    await asyncio.sleep(delay)
    loop.create_task(task)


def print_func_info(*args):
    print(inspect.stack()[1][3])
    for i in args:
        print(i)