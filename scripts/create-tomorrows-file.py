#!/usr/bin/env python3

"""
Compose a tweet for the latest addition to the posts directory.
"""

import os
import glob


contents = open("./_drafts/_tmp.md", 'r').read()

latest_post = int((
    max(glob.glob("./_posts/*.md"))
).split('.')[1].split('-')[-1])

latest_draft = int((
    max([fname for fname in
        glob.glob("./_drafts/*.md")
        if "_tmp" not in fname
    ] + ["./_drafts/0.md"])
).split('.')[-2].split('/')[2])

new_post = max([latest_draft, latest_post]) + 1


newfile = "./_drafts/{}.md".format(new_post)

with open(newfile, 'w') as fh:
    fh.write(contents)
