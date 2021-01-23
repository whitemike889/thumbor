#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

from datetime import datetime
from os import fstat
from os.path import abspath, exists, join

from thumbor.loaders import LoaderResult


def load(context, path, callback):
    file_path = join(context.config.FILE_LOADER_ROOT_PATH.rstrip("/"), path.lstrip("/"))
    file_path = abspath(file_path)
    inside_root_path = file_path.startswith(context.config.FILE_LOADER_ROOT_PATH)

    result = LoaderResult()

    if inside_root_path and exists(file_path):

        with open(file_path, "rb") as loaded_file:
            stats = fstat(loaded_file.fileno())

            result.successful = True
            result.buffer = loaded_file.read()

            result.metadata.update(
                size=stats.st_size, updated_at=datetime.utcfromtimestamp(stats.st_mtime)
            )
    else:
        result.error = LoaderResult.ERROR_NOT_FOUND
        result.successful = False

    callback(result)
