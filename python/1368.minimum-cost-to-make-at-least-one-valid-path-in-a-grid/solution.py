# Created by none at 2025/01/18 15:28
# leetgo: 1.4.13
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

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
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * n for _ in range(m)]
        f[0][0] = 0
        dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        q = deque([(0, 0, 0)])
        while q:
            x, y, c = q.popleft()
            if x == m - 1 and y == n - 1:
                return c
            dx, dy = dirs[grid[x][y]]
            nx, ny = x + dx, y + dy
            if valid(nx, ny) and f[nx][ny] > c:
                f[nx][ny] = c
                q.appendleft((nx, ny, c))
            for dx, dy in dirs[1:]:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and f[nx][ny] > c + 1:
                    f[nx][ny] = c + 1
                    q.append((nx, ny, c + 1))
        raise NotImplementedError


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minCost(grid)
    print("\noutput:", serialize(ans, "integer"))
