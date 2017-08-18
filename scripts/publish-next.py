#!/usr/bin/env python

import os
import datetime

post_num = len(os.listdir("./_posts")) + 1
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

dest_file = "{}-{}.md".format(date_str, post_num)


file_to_move = sorted(os.listdir("./_drafts"))[0]

os.rename(file_to_move, dest_file)
