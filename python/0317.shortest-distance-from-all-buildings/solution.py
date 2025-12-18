# Created by none at 2025/05/28 21:09
# leetgo: dev
# https://leetcode.com/problems/shortest-distance-from-all-buildings/

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
    def shortestDistance(self, grid: List[List[int]]) -> int | float:
        dirs = [0, -1, 0, 1, 0]
        m, n = len(grid), len(grid[0])
        cnt = [[0] * n for _ in range(m)]
        f = [[0] * n for _ in range(m)]  # sum dist (house to empty)

        def bfs(x: int, y: int):
            dist = [[inf] * n for _ in range(m)]
            q = deque([(0, x, y)])
            dist[x][y] = 0
            while q:
                d, x, y = q.popleft()
                for dx, dy in pairwise(dirs):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] == 0 and dist[nx][ny] == inf:
                        dist[nx][ny] = d + 1
                        cnt[nx][ny] += 1  # empty can be arrived by house
                        f[nx][ny] += dist[nx][ny]  # add dist (house to empty)
                        q.append((dist[nx][ny], nx, ny))

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    bfs(i, j)

        res = inf
        total_house = sum(1 for row in grid for x in row if x == 1)
        for i in range(m):
            for j in range(n):
                if cnt[i][j] == total_house:
                    res = min(res, f[i][j])
        return res if res != inf else -1

        # def bfs(x: int, y: int):
        #     dist = [[inf] * n for _ in range(m)]
        #     q = deque([(0, x, y)])
        #     dist[x][y] = 0
        #     cnt = buildings
        #     res = 0
        #     while q and cnt > 0:
        #         d, x, y = q.popleft()
        #         for dx, dy in pairwise(dirs):
        #             nx, ny = x + dx, y + dy
        #             if (
        #                 0 <= nx < m
        #                 and 0 <= ny < n
        #                 and grid[nx][ny] != 2
        #                 and dist[nx][ny] == inf
        #             ):
        #                 dist[nx][ny] = d + 1
        #                 if grid[nx][ny] == 1:
        #                     res += dist[nx][ny]
        #                     cnt -= 1
        #                 else:
        #                     q.append((dist[nx][ny], nx, ny))
        #     return res if cnt == 0 else inf

        # res = inf
        # for i, row in enumerate(grid):
        #     for j, x in enumerate(row):
        #         if x != 0:
        #             continue
        #         res = min(res, bfs(i, j))
        # return -1 if res == inf else res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestDistance(grid)
    print("\noutput:", serialize(ans, "integer"))
