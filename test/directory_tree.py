#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
directory = '/home/nick'
for (path, dirs, files) in os.walk(directory):
    print path