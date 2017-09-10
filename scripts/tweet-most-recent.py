#!/usr/bin/env python3

"""
Compose a tweet for the latest addition to the posts directory.
"""

import os
import glob
import yaml


def main():
    """
    Print the tweet.

    TODO: Integrate with `t` (npm i -G t) to auto-tweet.
    """
    latest_post = max(glob.glob("./_posts/*.md"))
    # latest_post = max(glob.glob("./_posts/*.md"), key=os.path.getctime)

    lines = open(latest_post, "r").readlines()

    info = yaml.load(
        "".join(lines[1:lines.index("---\n", 2)])
    )

    if "arxiv" in info:
        info["aux_url"] = "https://arxiv.org/abs/" + info['arxiv']

    if "doi" in info:
        info["aux_url"] = "https://doi.org/" + info['doi']

    if "uri" in info:
        info["aux_url"] = info['uri']

    info["url"] = "http://blog.jordan.matelsky.com/365papers/{}/".format(
        latest_post.split(".")[-2].split("-")[-1]
    )

    tweet = "New #365papers post: {title} {url} {aux_url}".format(**info)
    print(tweet)

if __name__ == "__main__":
    main()
