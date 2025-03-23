# Created by none at 2025/03/23 13:01
# leetgo: 1.4.13
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import *
from typing import List, Optional

from leetgo_py import *


# @lc code=begin
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, t in roads:
            g[x].append((y, t))
            g[y].append((x, t))

        dist = [inf] * n
        dist[0] = 0
        res = [0] * n
        res[0] = 1

        q = [(0, 0)]
        while q:
            min_t, x = heappop(q)
            for y, t in g[x]:
                cur_t = min_t + t
                if cur_t < dist[y]:
                    dist[y] = cur_t
                    res[y] = res[x]
                    heappush(q, (cur_t, y))
                elif cur_t == dist[y]:
                    res[y] += res[x]
                    res[y] %= 10**9 + 7
        return res[-1]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)
    print("\noutput:", serialize(ans, "integer"))
