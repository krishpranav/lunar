import urllib.request
import os
import gzip
import shutil
from pathlib import Path

class Download:
    @staticmethod
    def get_cache_path():
        home = str(Path.home())
        cachedir = f"{home}/.lunar"
        return cachedir

    @staticmethod
    def get_url_content(url: str):
        with urllib.request.urlopen(url) as url_response:
            content = url_response.read().decode()
            return content

    '''
    method: get contents in a file
    '''
    @staticmethod
    def get_file_content(path: str):
        with open(path, "r") as file:
            content = file.read()
            return content

