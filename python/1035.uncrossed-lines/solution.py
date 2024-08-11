# Created by none at 2024/08/11 12:37
# leetgo: 1.4.7
# https://leetcode.cn/problems/uncrossed-lines/

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
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        @functools.cache
        def dfs(i: int, j: int):
            if i == m or j == n:
                return 0
            return max(
                int(nums1[i] == nums2[j]) + dfs(i + 1, j + 1),
                dfs(i, j + 1),
                dfs(i + 1, j),
            )

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxUncrossedLines(nums1, nums2)
    print("\noutput:", serialize(ans, "integer"))
