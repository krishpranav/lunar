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

    @staticmethod
    def get_file_content(path: str):
        with open(path, "r") as file:
            content = file.read()
            return content

    @staticmethod
    def needs_download(file_path: str, force: bool = False) -> bool:
        if not os.path.isfile(file_path):
            result = True
        else:
            stats = os.stat(file_path)
            size = stats.st_size
            result = force or size == 0
        return result

    @staticmethod
    def download_file(
        url: str, file_name: str, target_directory: str, force: bool = False
    ):
        if Download.needs_download(target_directory, force):
            file_path = f"{target_directory}/{file_name}"
            urllib.request.urlretrieve(url, file_path)

    @staticmethod
    def download_backup_file(
        url: str, file_name: str, target_directory: str, force: bool = False
    ):
        extract_to = f"{target_directory}/{file_name}"
        if Download.needs_download(extract_to, force=force):
            if not os.path.isdir(target_directory):
                os.makedirs(target_directory)
            zipped = f"{extract_to}.gz"
            print(f"Downloading {zipped} from {url} ... this might take a few seconds")
            urllib.request.urlretrieve(url, zipped)
            print(f"Unzipping {extract_to} from {zipped}")
            with gzip.open(zipped, "rb") as gzipped:
                with open(extract_to, "wb") as unzipped:
                    shutil.copyfileobj(gzipped, unzipped)
                print("Extracting completed")
            if not os.path.isfile(extract_to):
                raise (f"could not extract {file_name} from {zipped}")
        return extract_to