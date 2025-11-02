# Created by none at 2025/11/02 11:11
# leetgo: dev
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

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
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        board = [[0] * n for _ in range(m)]
        for x, y in guards:
            board[x][y] = 1
        for x, y in walls:
            board[x][y] = 2

        def dfs(x: int, y: int, dx: int, dy: int):
            x += dx
            y += dy
            if not (0 <= x < m and 0 <= y < n):
                return
            if board[x][y] == 2 or board[x][y] == 1:
                return
            board[x][y] = 3
            dfs(x, y, dx, dy)

        dirs = [0, 1, 0, -1, 0]
        for x, y in guards:
            for dx, dy in pairwise(dirs):
                dfs(x, y, dx, dy)

        return sum(x == 0 for row in board for x in row)


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    guards: List[List[int]] = deserialize("List[List[int]]", read_line())
    walls: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countUnguarded(m, n, guards, walls)
    print("\noutput:", serialize(ans, "integer"))
