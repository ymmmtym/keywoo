#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import sys

r = requests.get(sys.argv[1])

text = r.text

for line in text.split("\n"):
    if '<title>' in line or '<h1>' in line:
        print(line.strip())
