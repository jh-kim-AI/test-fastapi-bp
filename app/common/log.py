# -*- coding: utf-8 -*-
import os
from typing import TYPE_CHECKING

from app.core import path_conf
from app.core.conf import settings

if TYPE_CHECKING:
    import loguru


class Logger:
    def __init__(self):
        self.log_path = path_conf.LogPath

    def log(self) -> loguru.Logger:
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        # Log file path
        log_stdout_path = os.path.join(self.log_path, settings.LOG_STDOUT_FILENAME)