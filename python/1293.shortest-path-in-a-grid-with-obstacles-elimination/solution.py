# Created by none at 2025/06/17 14:01
# leetgo: dev
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

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
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        q = [(0, 0, 0, K)]
        visited = [[-1] * n for _ in range(m)]  # how many obstacles can be eliminated
        visited[0][0] = K

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        dirs = [0, 1, 0, -1, 0]
        while q:
            d, x, y, k = heappop(q)
            if x == m - 1 and y == n - 1:
                return d
            for dx, dy in pairwise(dirs):
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and (grid[nx][ny] == 0 or k > 0):
                    pair = (d + 1, nx, ny, k - grid[nx][ny])
                    if visited[nx][ny] < pair[-1]:
                        visited[nx][ny] = pair[-1]
                        heappush(q, pair)

        return -1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().shortestPath(grid, k)
    print("\noutput:", serialize(ans, "integer"))
