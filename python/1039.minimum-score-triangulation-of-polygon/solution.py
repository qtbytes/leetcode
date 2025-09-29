# Created by none at 2025/09/29 09:56
# leetgo: dev
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

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
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(a: tuple[int]):
            n = len(a)
            if n < 3:
                return 0
            if n == 3:
                return a[0] * a[1] * a[2]
            res = inf
            # select a point, x to from triangle [a[0], a[-1], x]
            # x and y can't adjant
            for x in range(1, n - 1):
                part1 = a[: x + 1]
                part2 = a[x:n]
                # print(part1, part2)
                res = min(res, a[0] * a[-1] * a[x] + dfs(part1) + dfs(part2))
            return res

        return dfs(tuple(values))


# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minScoreTriangulation(values)
    print("\noutput:", serialize(ans, "integer"))
