#!/usr/bin/env python3

data = None
with open("./scripts/pages-hits.csv", "r") as fh:
    data = [d.split(",") for d in fh.readlines()]

print(data)
