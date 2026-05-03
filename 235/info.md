- Initially I thought it would be a good idea to look
    for `p` and `q` from from each node and send to left if found to try to minimize the result
- After running a couple of examples I was able to identify the pattern that the LCA would always be
in between `p` and `q`, so `min(p, q) <= LCA <= max(p, q)`

