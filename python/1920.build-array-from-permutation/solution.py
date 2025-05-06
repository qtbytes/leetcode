# Created by none at 2025/05/06 11:56
# leetgo: 1.4.13
# https://leetcode.com/problems/build-array-from-permutation/

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
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        delta = 2 * n
        for i in range(n):
            if nums[i] >= delta:
                continue
            start = nums[i]
            while nums[i] < delta and nums[nums[i]] < delta:
                x = nums[i]
                nums[i] = nums[x] + delta
                i = x
            nums[i] = start + delta
            # print([x - delta for x in nums])
        for i, x in enumerate(nums):
            nums[i] = x - delta
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
