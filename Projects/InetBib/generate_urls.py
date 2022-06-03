#!/usr/bin/env python

"""
https://www.inetbib.de/listenarchiv/msg70057.html
"""

max_id = 70057
for i in range(1, max_id + 1):
    url = "https://www.inetbib.de/listenarchiv/msg{:05d}.html".format(i)
    print(url)
