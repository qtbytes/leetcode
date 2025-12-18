# Created by none at 2024/09/08 12:45
# leetgo: 1.4.9
# https://leetcode.cn/problems/squares-of-a-sorted-array/

import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import string
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def sortedSquares(self, nums: list[int]) -> List[int]:
        j = bisect.bisect_left(nums, 0)  # ty:ignore
        i = j - 1
        res = []
        n = len(nums)
        while i >= 0 or j < n:
            if i == -1 or (j < n and nums[j] <= -nums[i]):
                res.append(pow(nums[j], 2))
                j += 1
            else:
                res.append(pow(nums[i], 2))
                i -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedSquares(nums)
    print("\noutput:", serialize(ans, "integer[]"))
