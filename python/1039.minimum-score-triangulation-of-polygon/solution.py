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
    def minScoreTriangulation(self, a: List[int]) -> int:
        @cache
        def dfs(l: int, r: int):
            size = r - l + 1
            if size < 3:
                return 0
            if size == 3:
                return a[l] * a[l + 1] * a[l + 2]
            res = inf
            for x in range(l + 1, r):
                res = min(res, a[l] * a[r] * a[x] + dfs(l, x) + dfs(x, r))
            return res

        return dfs(0, len(a) - 1)


# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minScoreTriangulation(values)
    print("\noutput:", serialize(ans, "integer"))
