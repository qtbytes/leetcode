# Created by none at 2025/06/16 23:17
# leetgo: dev
# https://leetcode.com/problems/cut-off-trees-for-golf-event/

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
    def cutOffTree(self, forest: List[List[int]]) -> int:
        tree = []
        for i, row in enumerate(forest):
            for j, x in enumerate(row):
                if x > 1:
                    tree.append((i, j))
        tree.sort(key=lambda p: forest[p[0]][p[1]])
        tree.insert(0, (0, 0))

        dirs = [0, 1, 0, -1, 0]
        m, n = len(forest), len(forest[0])

        def valid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n

        def bfs(start, end) -> int:
            visited = [[-1] * n for _ in range(m)]
            x, y = start
            q = deque([(x, y)])
            visited[x][y] = 0

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if (x, y) == end:
                        return visited[x][y]
                    for dx, dy in pairwise(dirs):
                        nx, ny = x + dx, y + dy
                        if (
                            valid(nx, ny)
                            and forest[nx][ny] != 0
                            and visited[nx][ny] == -1
                        ):
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
            return -1

        res = 0

        for start, end in pairwise(tree):
            sub = bfs(start, end)
            if sub == -1:
                return -1
            res += sub
        return res


# @lc code=end

if __name__ == "__main__":
    forest: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().cutOffTree(forest)
    print("\noutput:", serialize(ans, "integer"))
