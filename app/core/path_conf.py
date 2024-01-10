# -*- coding: utf-8 -*-
import os
from pathlib import Path

# project root directory
# or absolute path to project root directory
BasePath = Path(__file__).resolve().parent.parent

# logfile path
LogPath = os.path.join(BasePath, 'app', 'log')
