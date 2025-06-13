# Created by none at 2025/06/13 10:16
# leetgo: dev
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

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
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        q = list(y - x for x, y in pairwise(nums))

        def check(x: int):
            i = 0
            n = len(q)
            cnt = 0
            while i < n:
                if q[i] <= x:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p

        l, r = 0, nums[-1]
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    p: int = deserialize("int", read_line())
    ans = Solution().minimizeMax(nums, p)
    print("\noutput:", serialize(ans, "integer"))
