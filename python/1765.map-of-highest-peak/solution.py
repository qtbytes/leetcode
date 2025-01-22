# Created by none at 2025/01/22 15:00
# leetgo: 1.4.13
# https://leetcode.com/problems/map-of-highest-peak/

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
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dirs = [0, 1, 0, -1, 0]
        q = []
        for i, row in enumerate(isWater):
            for j, x in enumerate(row):
                if x == 1:
                    q.append((i, j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = inf
        m, n = len(isWater), len(isWater[0])
        while q:
            p = []
            for x, y in q:
                for dx, dy in pairwise(dirs):
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and isWater[nx][ny] > isWater[x][y] + 1
                    ):
                        isWater[nx][ny] = isWater[x][y] + 1
                        p.append((nx, ny))
            q = p
        return isWater


# @lc code=end

if __name__ == "__main__":
    isWater: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().highestPeak(isWater)
    print("\noutput:", serialize(ans, "integer[][]"))
