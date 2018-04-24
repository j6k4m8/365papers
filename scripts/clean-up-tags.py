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

distances = np.ndarray((len(tags), len(tags)))

for i in range(len(tags)):
	for j in range(len(tags)):
		if i is not j:
			distances[i,j] = editdistance.eval(
				tags[i].lower(), tags[j].lower()
			)
			if tags[i].lower() == tags[j].lower():
				distances[i,j] = 1
		else:
			distances[i,j] = 99

tag_pairs = [
	(tags[i], tags[j])
	for i, j in zip(*np.where(distances <= 1))
        if len(tags[i]) > 4
]

tag_pairs = [
	t for t in tag_pairs if tag_counts[t[0]] < tag_counts[t[1]]
]

if len(tag_pairs) is 0:
    exit()

print("\n".join([
	"{}: {} ({}) -> {} ({})".format(i, t[0], len(tag_associations[t[0]]), t[1], len(tag_associations[t[1]]))
	for i, t in enumerate(tag_pairs)
]))

i = None
while i != 'q':
	i = input("?> ")
	if i == 'q':
		break

	i = int(i)

	for f in tag_associations[tag_pairs[i][0]]:
		lines = open(f, 'r').readlines()
		lines[lines.index(
			"    - " + tag_pairs[i][0] + "\n"
		)] = "    - " + tag_pairs[i][1] + "\n"
		with open(f, 'w') as fh:
			fh.writelines(lines)


# plt.imshow(distances)
# plt.show()
