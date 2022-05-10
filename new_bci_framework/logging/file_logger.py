import atexit
import time
from typing import IO

from new_bci_framework.logging import Logger


class FileLogger(Logger):

    def __init__(self, file_path: str, overwrite=True):
        super().__init__()
        self.__log_path = file_path
        self.__mode = 'w' if overwrite else 'a'
        self.__file: IO = open(file_path, self.__mode)
        atexit.register(lambda: self.__file.close())

    def log(self, tag="GENERAL", message="", importance=1):
        # if not hasattr(self, "__file"):
        #     raise RuntimeError("FileLogger incorrect usage. Use 'with FileLogger(path) as...'")
        importance_level = "INFO"
        self.__file.write(f"{time.asctime()}-{importance_level}-{tag}: {message}\n")

    # def __enter__(self):
    #     self.__file = open(self.__log_path, self.__mode)
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.__file.close()
