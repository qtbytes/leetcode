# Created by none at 2024/08/30 21:58
# leetgo: 1.4.7
# https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/

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
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)

        def handle(cnt: list[int]):
            return sum(x * (n - x) for x in cnt) // 2

        d = len(str(nums[0]))
        bits = [[0] * 10 for _ in range(d)]
        for x in nums:
            for i in range(d):
                bits[i][x % 10] += 1
                x //= 10

        return sum(handle(bit) for bit in bits)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumDigitDifferences(nums)
    print("\noutput:", serialize(ans, "long"))
