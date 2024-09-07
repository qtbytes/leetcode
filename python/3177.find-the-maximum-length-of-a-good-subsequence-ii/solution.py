# Created by none at 2024/09/07 12:38
# leetgo: 1.4.9
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-ii/

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
    def maximumLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return max(collections.Counter(nums).values())

        f = [collections.defaultdict(int) for _ in range(k + 1)]
        mx = [0] * (k + 1)

        # f[j][x] = 1 + max(f[j - 1][y], f[j][x])
        for x in nums:
            for j in range(k, -1, -1):
                f[j][x] = 1 + max(f[j][x], mx[j - 1] if j > 0 else 0)
                mx[j] = max(mx[j], f[j][x])
        return max(mx)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))
