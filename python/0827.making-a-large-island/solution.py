# Created by none at 2025/01/31 23:21
# leetgo: 1.4.13
# https://leetcode.com/problems/making-a-large-island/

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
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [0, 1, 0, -1, 0]

        def dfs(x: int, y: int, t: int):
            res = 0
            if not (0 <= x < m and 0 <= y < n):
                return res
            if grid[x][y] == 1:
                grid[x][y] = t
                res += 1
                for dx, dy in pairwise(dirs):
                    res += dfs(x + dx, y + dy, t)
            return res

        t = 2
        size = {}
        size[0] = 0

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size[t] = dfs(i, j, t)
                    res = max(res, size[t])
                    t += 1

        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                g = set()
                if ch == 0:
                    for dx, dy in pairwise(dirs):
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n:
                            g.add(grid[x][y])
                res = max(res, 1 + sum(size[t] for t in g))
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestIsland(grid)
    print("\noutput:", serialize(ans, "integer"))
