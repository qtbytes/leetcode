# Created by none at 2025/01/29 10:27
# leetgo: 1.4.13
# https://leetcode.com/problems/redundant-connection/

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        fa = list(range(n + 1))

        def find(x: int):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            fa[fy] = fx
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]

        return []


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findRedundantConnection(edges)
    print("\noutput:", serialize(ans, "integer[]"))
