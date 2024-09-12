# Created by none at 2024/09/12 11:05
# leetgo: 1.4.9
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/

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
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        if n == 1:
            return res
        nums.sort()
        mid = (n - 1) >> 1
        l = mid
        r = n - 1
        while l >= 0 and r > mid:
            if nums[l] * 2 <= nums[r]:
                res += 2
                r -= 1
            l -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumOfMarkedIndices(nums)
    print("\noutput:", serialize(ans, "integer"))
