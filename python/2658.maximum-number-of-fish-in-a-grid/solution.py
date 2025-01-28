# Created by none at 2025/01/28 13:57
# leetgo: 1.4.13
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

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
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        N = m * n
        fa = list(range(N))

        def find(x: int):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int) -> int:
            fx, fy = find(x), find(y)
            fa[fy] = fx

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                idx = i * n + j
                if x > 0:
                    if j + 1 < n and row[j + 1] > 0:
                        union(idx, idx + 1)
                    if i + 1 < m and grid[i + 1][j] > 0:
                        union(idx, idx + n)

        res = [0] * N

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x > 0:
                    res[find(i * n + j)] += x

        return max(res)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMaxFish(grid)
    print("\noutput:", serialize(ans, "integer"))
