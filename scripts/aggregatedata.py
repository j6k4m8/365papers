import glob
import json
import re
import os

import numpy as np
import pandas as pd
import yaml
import networkx as nx


def construct_posts(
        posts_glob: str = "../_posts/*.md",
        page_hits_path: str = "./pages-hits.csv"
) -> pd.DataFrame:
    _posts = []
    _postfiles = glob.glob(posts_glob)
    yaml.reader.Reader.NON_PRINTABLE = re.compile(
        u'[^\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]'
    )
    for file in _postfiles:
        try:
            _, frontmatter, text = open(file, 'r').read().split("---")
        except:
            print(f"Failed to parse frontmatter in {file}, probably had '---' in text")
        parsed_frontmatter = yaml.load(frontmatter)
        parsed_frontmatter['text'] = text.strip()
        
        fname = os.path.basename(file).split(".")[0]
        year, month, day, index = fname.split("-")
        parsed_frontmatter['date'] = pd.datetime(int(year), int(month), int(day))
        parsed_frontmatter['index'] = int(index)
        _posts.append(parsed_frontmatter)
    
    posts = pd.DataFrame(_posts)
    posts.set_index('index', inplace=True)
    
    hits = pd.read_csv("./pages-hits.csv")
    hits['index'] = hits.Page.str.strip("/")
    hits.set_index('index', inplace=True)
    hits.dropna(inplace=True)
    hits = hits[hits.index.str.isnumeric()]
    hits.index = hits.index.astype(int)

    posts = posts.join(hits)
    # post-processing: (heh)
    posts.Pageviews.fillna(inplace=True, value=0)
    posts.Pageviews = posts.Pageviews.astype(float)
    
    posts['href'] = posts.index.map(lambda x: "https://blog.jordan.matelsky.com/365papers/{}".format(x))
    return posts

def construct_tags(posts: pd.DataFrame) -> pd.DataFrame:
    """
    Construct a dataframe of tags
    """
    _tags = {}
    for i, post in posts.iterrows():
        for tag in post.tags:
            if tag in _tags:
                _tags[tag]['posts'].append(i)
            else:
                _tags[tag] = {
                    'text': tag,
                    'posts': [i],
                    'href': "https://blog.jordan.matelsky.com/365papers/tag/#{}".format(tag)
                }
    tags = pd.DataFrame(_tags).T
    
    tags['usecount'] = tags.posts.map(lambda x: len(x))
    tags['viewcount'] = tags.posts.map(lambda T: np.sum([posts.loc[x].Pageviews if (x == []) else 0 for x in T]))
    return tags