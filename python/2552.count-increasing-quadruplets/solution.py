# Created by none at 2024/09/10 12:28
# leetgo: 1.4.9
# https://leetcode.cn/problems/count-increasing-quadruplets/

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
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        - `4 <= nums.length <= 4000`
        - `1 <= nums[i] <= nums.length`
        - All the integers of `nums` are **unique**. `nums` is a permutation.
        """

        n = len(nums)
        dp = [0] * n
        res = 0
        for l, x in enumerate(nums):
            cnt_i = 0
            for j in range(l):
                if x > nums[j]:
                    res += dp[j]
                    cnt_i += 1
                else:
                    dp[j] += cnt_i
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countQuadruplets(nums)
    print("\noutput:", serialize(ans, "long"))
