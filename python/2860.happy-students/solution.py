# Created by none at 2024/09/04 20:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/happy-students/

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
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            res += (nums[i] < i + 1) and (i + 1 >= n or i + 1 < nums[i + 1])
        return res + (nums[0] > 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countWays(nums)
    print("\noutput:", serialize(ans, "integer"))
