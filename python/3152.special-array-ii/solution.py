# Created by none at 2024/08/14 10:37
# leetgo: 1.4.7
# https://leetcode.cn/problems/special-array-ii/

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
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        a = []
        i, n = 0, len(nums)

        while i < n:
            j = i + 1
            while j < n and nums[j] & 1 != nums[j - 1] & 1:
                j += 1
            a.append((i, j - 1))
            i = j

        # we can record valid left border for each index
        # then don't need binary search
        def f(x: int, y: int):
            # [x,y] should not intersect with more than one segments
            i = bisect.bisect_left(a, y, key=lambda e: e[1])
            return a[i][0] <= x

        return [f(*q) for q in queries]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isArraySpecial(nums, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
