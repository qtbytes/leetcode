# Created by none at 2025/05/17 13:08
# leetgo: dev
# https://leetcode.com/problems/sort-colors/

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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cnt = [0] * 3
        # for x in nums:
        #     cnt[x] += 1
        # j = 0
        # for i in range(len(nums)):
        #     while cnt[j] == 0:
        #         j += 1
        #     nums[i] = j
        #     cnt[j] -= 1

        l = i = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
