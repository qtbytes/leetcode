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
        # top_left = [[False] * n for _ in range(m)]
        # bot_right = [[False] * n for _ in range(m)]

        res = []

        def dfs(x: int, y: int):
            top_left = bot_right = False
            if x == 0 or y == 0:
                top_left = True
            if x == m - 1 or y == n - 1:
                bot_right = True

            if (x, y) in visited:
                return visited[(x, y)]
            # tag as visited
            visited[(x, y)] = (top_left, bot_right)
            if top_left and bot_right:
                return True, True

            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[x][y] >= heights[nx][ny]:
                    sub = dfs(nx, ny)
                    top_left |= sub[0]
                    bot_right |= sub[1]

            return top_left, bot_right

        for x in range(m):
            for y in range(n):
                visited = dict()
                if all(ok for ok in dfs(x, y)):
                    res.append([x, y])

        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().pacificAtlantic(heights)
    print("\noutput:", serialize(ans, "integer[][]"))
