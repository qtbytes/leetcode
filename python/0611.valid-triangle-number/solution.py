# Created by none at 2025/09/26 12:39
# leetgo: dev
# https://leetcode.com/problems/valid-triangle-number/

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
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i < n and nums[i] == 0:
            i += 1
        nums = nums[i:]
        n = len(nums)

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # nums[i] + nums[j] > nums[k]
                # while k < n and nums[i] + nums[j] >= nums[k]:
                # k += 1
                k = bisect_left(nums, nums[i] + nums[j])
                # print(i, j, k, nums)
                # can use [j+1:k]
                res += k - j - 1
                # early stop
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().triangleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
