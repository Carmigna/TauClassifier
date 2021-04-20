"""
Utilities
___________________________________________
File containing useful functions and classes
"""

import time
from enum import Enum
from functools import total_ordering
from datetime import datetime
import os
from inspect import getframeinfo, stack


@total_ordering
class LogLevels(Enum):
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    HELPME = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Logger:

    def __init__(self, log_level='INFO'):
        self._start_time = time.time()
        self._log_level = LogLevels[log_level]

    def log(self, message, level='INFO'):
        if LogLevels[level] <= self._log_level:
            time_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            caller = getframeinfo(stack()[1][0])
            filename = caller.filename
            line_num = caller.lineno
            filename = os.path.basename(filename)
            print(f"{time_now} {filename}:{line_num} {level} - {message}")

    def set_log_level(self, level):
        self._log_level = LogLevels[level]

# Initialize logger as global variable
logger = Logger()

