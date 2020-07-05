# -*- Coding: utf-8 -*-
# Author: Yu

import yaml
import os
from unit.path_config import request_path


class yaml_handle_cls:

    @classmethod
    def yaml_load(cls, filename) -> list:
        path = os.path.join(request_path, filename)
        with open(path) as f:
            return yaml.safe_load(f)
