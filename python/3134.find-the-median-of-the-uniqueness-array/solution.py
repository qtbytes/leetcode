# Created by none at 2024/08/27 13:42
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/

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
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = n * (n + 1) // 2

        def check(mid):
            seen = collections.defaultdict(int)
            l = 0
            cnt = 0
            diff = 0
            for r, x in enumerate(nums):
                seen[x] += 1
                if seen[x] == 1:
                    diff += 1
                while diff > mid:
                    seen[nums[l]] -= 1
                    if seen[nums[l]] == 0:
                        diff -= 1
                    l += 1
                cnt += r - l + 1
            return cnt >= (m + 1) // 2

        l = 1
        r = n // 2 + 1
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().medianOfUniquenessArray(nums)
    print("\noutput:", serialize(ans, "integer"))
