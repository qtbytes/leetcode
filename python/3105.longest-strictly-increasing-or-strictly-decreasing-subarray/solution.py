# Created by none at 2025/02/03 12:27
# leetgo: 1.4.13
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

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
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        i = 0

        def mono(j: int):
            return (nums[j + 1] - nums[j]) * (nums[j] - nums[j - 1]) > 0

        while i + 1 < n:
            j = i + 1
            if nums[i] != nums[j]:
                while j + 1 < n and mono(j):
                    j += 1
                res = max(res, j - i + 1)
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestMonotonicSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
