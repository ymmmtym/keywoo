#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import wave

argvs = sys.argv

wf = wave.open(argvs[1], 'rb')

print(wf.getnchannels())
print(wf.getsampwidth())
print(wf.getframerate())
print(wf.getframes())
