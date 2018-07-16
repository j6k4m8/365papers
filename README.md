# 365papers
> A paper per day has no effect on doctor proximity (p &lt; 0.05).

## I want to do this. How?

- Clone this repository
- Modify `_config.yml` to say your name instead of my name
- Enable GitHub Pages support (https://github.com/[YOUR_USERNAME]/365papers/settings)
- Confirm the site works: https://[YOUR_USERNAME].github.io/365papers
- Optionally set up a CNAME: https://help.github.com/articles/using-a-custom-domain-with-github-pages/
- Let me know when you're done so I can check it out!!
- Give me credit for writing the website design code if you feel like being nice :)

## Scripts

**Pro-tip: Use `./submit.sh`. it runs all of the following:**

`publish-next.py` moves the next file from `_drafts/` to `_posts/` and renames it according to the blog-post naming convention used by Jekyll. If you have `11.md` and `12.md` in your drafts folder, this will make `(today's-date)-11.md` in your posts directory.

`clean-up-tags.py` confirms that your high-similarity tags are actually supposed to be what you typed; so it'll ask if `frendship`, which you've only tagged once, is supposed to be `friendship`, which you've tagged twenty times. **To quit, use `q` (enter).** To replace, type the number of the row you want to replace.

`tweet-most-recent.py` prints a tweet version of the paper's title and the `#365papers` hashtag. I usually pipe this to `pbcopy`.

`create-tomorrows-file.py` creates the next consecutive file for whatever number post is one greater than the current maximum; so if you have posts 1, 2, and 3, and drafts 4 and 5, this script will generate `6.md` in the drafts directory.

## My usual workflow

```
./submit.sh
```

OR:

```
./scripts/publish-next.py && ./scripts/clean-up-tags.py && ./scripts/tweet-most-recent.py | pbcopy && git add _posts/ && git commit -m "New post $(date +%Y-%m-%d)" && git push
```
