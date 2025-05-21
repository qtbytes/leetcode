# Created by none at 2024/09/03 11:02
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-strength-of-a-group/

from typing import *
from leetgo_py import *

import bisect
import collections
import functools
import heapq
import itertools
import operator
import math
import string

# @lc code=begin


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if all(x == 0 for x in nums):
            return 0
        a = []
        res = 1
        zero = 0
        for x in nums:
            if x == 0:
                zero += 1
            elif x > 0:
                res *= x
            else:
                a.append(x)
        if len(a) & 1 == 0:
            return res * functools.reduce(operator.mul, a, 1)
        if len(a) == 1 and zero + len(a) == len(nums):
            return 0
        a.sort(reverse=True)
        return res * functools.reduce(operator.mul, a[1:], 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxStrength(nums)
    print("\noutput:", serialize(ans, "long"))
