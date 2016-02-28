#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com


class Header(object):
    def __init__(self, headers):
        self.should_run = False
        if 'image/webp' in headers.get('Accept', ''):
            self.should_run = True

    def set_format(self, ctx):
        if not ctx.request.engine.is_multiple() and \
               ctx.request.engine.can_convert_to_webp() and \
               ctx.request.format is None:
            ctx.request.format = 'webp'

    def get_path_segment(self):
        return 'webp'
