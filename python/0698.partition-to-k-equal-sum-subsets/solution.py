# Created by none at 2024/08/25 17:25
# leetgo: 1.4.7
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/

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
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        nums.sort()
        if s % k != 0 or nums[-1] > s // k:
            return False

        n = len(nums)
        TARGET = s // k

        @functools.cache
        def dfs(target: int, mask: int, k: int):
            if k == 0:
                return mask == 0

            for i, x in enumerate(nums):
                if mask >> i & 1 and x <= target:
                    target_next = target - x
                    k_next = k
                    if target_next == 0:
                        target_next = TARGET
                        k_next -= 1
                    if dfs(target_next, mask ^ (1 << i), k_next):
                        return True
            return False

        return dfs(TARGET, (1 << n) - 1, k)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().canPartitionKSubsets(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
