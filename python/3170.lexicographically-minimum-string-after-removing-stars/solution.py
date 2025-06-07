# Created by none at 2025/06/07 11:56
# leetgo: dev
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def clearStars(self, s: str) -> str:
        p = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            if ch == "*":
                for v in p:
                    if v:
                        v.pop()
                        break
            else:
                p[ord(ch) - ord("a")].append(i)

        res = ["#"] * len(s)
        for i, v in enumerate(p):
            ch = chr(ord("a") + i)
            for idx in v:
                res[idx] = ch
        return "".join(ch for ch in res if ch != "#")


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().clearStars(s)
    print("\noutput:", serialize(ans, "string"))
