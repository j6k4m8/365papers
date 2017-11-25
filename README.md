# 365papers
> A paper per day has no effect on doctor proximity (p &lt; 0.05).



## Scripts

`publish-next.py` moves the next file from `_drafts/` to `_posts/` and renames it according to the blog-post naming convention used by Jekyll. If you have `11.md` and `12.md` in your drafts folder, this will make `(today's-date)-11.md` in your posts directory.

`clean-up-tags.py` confirms that your high-similarity tags are actually supposed to be what you typed; so it'll ask if `frendship`, which you've only tagged once, is supposed to be `friendship`, which you've tagged twenty times. **To quit, use `q` (enter)`.** To replace, type the number of the row you want to replace.

`tweet-most-recent.py` prints a tweet version of the paper's title and the `#365papers` hashtag. I usually pipe this to `pbcopy`.

`create-tomorrows-file.py` creates the next consecutive file for whatever number post is one greater than the current maximum; so if you have posts 1, 2, and 3, and drafts 4 and 5, this script will generate `6.md` in the drafts directory.

## My usual workflow

```
./scripts/publish-next.py && ./scripts/clean-up-tags.py && ./scripts/tweet-most-recent.py | pbcopy && git add _posts/ && git commit -m "New post $(date +%Y-%m-%d)" && git push
```
