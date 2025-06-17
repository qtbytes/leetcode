# Created by none at 2025/06/17 15:36
# leetgo: dev
# https://leetcode.com/problems/find-in-mountain-array/

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

"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""


class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, a: "MountainArray") -> int:
        # - `3 <= mountainArr.length() <= 10⁴`
        n = a.length()

        @cache
        def get(i: int) -> int:
            return a.get(i)

        l = 0
        r = n - 1
        while l < r:
            m = (l + r) >> 1
            if get(m) < get(m + 1):
                l = m + 1
            else:
                r = m

        top = l

        # check left
        l = 0
        r = top + 1
        while l < r:
            m = (l + r) >> 1
            if get(m) < target:
                l = m + 1
            else:
                r = m

        if get(l) == target:
            return l

        # check right
        l = top
        r = n
        while l < r:
            m = (l + r) >> 1
            if get(m) > target:
                l = m + 1
            else:
                r = m

        if l < n and get(l) == target:
            return l
        return -1


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    mountainArr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findInMountainArray(mountainArr, target)
    print("\noutput:", serialize(ans, "integer"))
