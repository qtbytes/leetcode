# Created by none at 2025/12/02 13:18
# leetgo: dev
# https://leetcode.com/problems/count-number-of-trapezoids-i/

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
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        cnt = defaultdict(int)
        for _, y in points:
            cnt[y] += 1
        pre = 0
        res = 0
        for c in cnt.values():
            cur = c * (c - 1) // 2
            res = (res + pre * cur) % mod
            pre += cur
        return res


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countTrapezoids(points)
    print("\noutput:", serialize(ans, "integer"))
