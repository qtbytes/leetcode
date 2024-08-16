# Created by none at 2024/08/16 10:15
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/

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
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)

        @functools.cache
        def dfs(i: int, j: int, x: int):
            if i == n:
                return 0 if j == m and x == -1 else math.inf
            if (x != -1 and x < andValues[j]) or j >= m:
                return math.inf
            res = dfs(i + 1, j, x & nums[i])
            if x & nums[i] == andValues[j]:
                res = min(res, nums[i] + dfs(i + 1, j + 1, -1))
            return res

        res = dfs(0, 0, -1)
        dfs.cache_clear()
        return res if res != math.inf else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    andValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumValueSum(nums, andValues)
    print("\noutput:", serialize(ans, "integer"))
