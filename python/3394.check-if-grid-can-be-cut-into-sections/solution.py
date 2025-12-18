# Created by none at 2025/03/25 19:25
# leetgo: 1.4.13
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

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
def handle_intervals(a: list[tuple[int, int]]) -> bool:
    a.sort()
    cnt = 0
    i, n = 0, len(a)
    while i < n:
        cnt += 1
        l, r = a[i]
        j = i + 1
        while j < n and a[j][0] < r:
            r = max(r, a[j][1])
            j += 1
        i = j
    return cnt >= 3


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizon = []
        vertical = []

        for sx, sy, ex, ey in rectangles:
            horizon.append((sx, ex))
            vertical.append((sy, ey))

        return handle_intervals(horizon) or handle_intervals(vertical)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValidCuts(n, rectangles)
    print("\noutput:", serialize(ans, "boolean"))
