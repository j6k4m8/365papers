#!/usr/bin/env python3

import subprocess

f = "./_posts/2017-09-01-11.md"

print(subprocess.getoutput(
    "/Library/Frameworks/Python.framework/Versions/3.6/bin/proselint " + f
))
