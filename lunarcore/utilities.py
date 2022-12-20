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

async def create_delayed_task(task, delay, loop):
    await asyncio.sleep(delay)
    loop.create_task(task)

def print_func_info(*args):
    print(insepct.stack()[1][3])
    for i in args:
        print(i)