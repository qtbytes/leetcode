# Created by none at 2025/10/05 13:00
# leetgo: dev
# https://leetcode.com/problems/pacific-atlantic-water-flow/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(x: int, y: int, f: list[list[bool]]):
            # can flow to border
            if f[x][y]:
                return
            f[x][y] = True
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                nx, ny = x + dx, y + dy
                # from lower to higher
                if 0 <= nx < m and 0 <= ny < n and heights[x][y] <= heights[nx][ny]:
                    dfs(nx, ny, f)

        top_left = [[False] * n for _ in range(m)]
        bot_right = [[False] * n for _ in range(m)]

        for j in range(n):
            dfs(0, j, top_left)
            dfs(m - 1, j, bot_right)
        for i in range(m):
            dfs(i, 0, top_left)
            dfs(i, n - 1, bot_right)

        res = []
        for i in range(m):
            for j in range(n):
                if top_left[i][j] and bot_right[i][j]:
                    res.append([i, j])
        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().pacificAtlantic(heights)
    print("\noutput:", serialize(ans, "integer[][]"))
