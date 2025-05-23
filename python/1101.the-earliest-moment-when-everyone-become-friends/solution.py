# Created by none at 2025/05/23 17:04
# leetgo: dev
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        fa = list(range(n))
        size = n

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if fx == fy:
                return
            nonlocal size
            size -= 1
            fa[fy] = fx

        logs.sort()
        for t, x, y in logs:
            union(x, y)
            if size == 1:
                return t
        return -1


# @lc code=end

if __name__ == "__main__":
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().earliestAcq(logs, n)
    print("\noutput:", serialize(ans, "integer"))
