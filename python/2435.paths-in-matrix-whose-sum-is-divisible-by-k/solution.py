# Created by none at 2025/11/26 23:11
# leetgo: dev
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

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
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        f = [[[0] * k for _ in range(n)] for _ in range(m)]
        f[0][0][grid[0][0] % k] = 1
        mod = 10**9 + 7

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                x %= k
                # move from top
                if i > 0:
                    for size in range(k):
                        f[i][j][size] = (
                            f[i][j][size] + f[i - 1][j][(size - x) % k]
                        ) % mod
                # move from left
                if j > 0:
                    for size in range(k):
                        f[i][j][size] = (
                            f[i][j][size] + f[i][j - 1][(size - x) % k]
                        ) % mod

        return f[m - 1][n - 1][0]


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfPaths(grid, k)
    print("\noutput:", serialize(ans, "integer"))
