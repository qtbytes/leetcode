# Created by none at 2024/08/21 13:35
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

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
    def findMaximumNumber(self, k: int, step: int) -> int:
        @functools.cache
        def dfs(x: int, step: int):
            if x == 0:
                return 0
            n = x.bit_length()
            cur = 1 << (n - 1)
            rest = x ^ cur
            res = dfs(rest, step) + dfs(cur - 1, step)
            if n % step == 0:
                res += rest + 1
            return res

        n = 1 << 60
        l, r = 1, n
        while l < r:
            mid = (l + r) >> 1
            if dfs(mid, step) <= k:
                l = mid + 1
            else:
                r = mid
        return l - 1


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findMaximumNumber(k, x)
    print("\noutput:", serialize(ans, "long"))
