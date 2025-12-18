# Created by none at 2025/06/17 16:37
# leetgo: dev
# https://leetcode.com/problems/first-missing-positive/

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
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x for x in nums if 0 < x <= len(nums)]

        n = len(nums)
        for i in range(n):
            x = abs(nums[i])
            if x <= n and nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]

        for i, x in enumerate(nums, 1):
            if x > 0:
                return i
        return n + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstMissingPositive(nums)
    print("\noutput:", serialize(ans, "integer"))
