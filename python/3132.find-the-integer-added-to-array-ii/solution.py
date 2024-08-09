# Created by none at 2024/08/09 12:40
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-integer-added-to-array-ii/

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
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)

        for mn in nums1[:3][::-1]:
            d = nums2[0] - mn
            i = j = 0
            while i < m and j < n:
                if nums1[i] + d == nums2[j]:
                    j += 1
                i += 1
            if j == n:
                return d


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumAddedInteger(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
