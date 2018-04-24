#!/usr/bin/env python3

import glob
import yaml
import re

import numpy as np
import matplotlib.pyplot as plt
import editdistance


files = glob.glob('./_posts/*.md')

tag_counts = {}
tag_associations = {}

for f in files:
	lines = open(f, 'r').readlines()
	try:
		info = yaml.load(
			"".join(lines[1:lines.index("---\n", 2)])
		)
		for t in info['tags']:
			if t not in tag_counts:
				tag_counts[t] = 0
				tag_associations[t] = []
			tag_counts[t] += 1
			tag_associations[t].append(f)

	except:
		pass

tags = sorted(list(set(list(tag_counts.keys()))))


print(tags)
