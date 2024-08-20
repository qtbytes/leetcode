# Created by none at 2024/08/20 12:37
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-number-of-ways-to-reach-the-k-th-stair/

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
    def waysToReachStair(self, k: int) -> int:
        @functools.cache
        def dfs(i: int, jump: int, back: bool):
            res = 0
            if i == k:
                res += 1
            if i > k and i - 1 > k:
                return res
            res += dfs(i + 2**jump, jump + 1, False)
            if not back:
                res += dfs(i - 1, jump, True)
            return res

        return dfs(1, 0, False)


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().waysToReachStair(k)
    print("\noutput:", serialize(ans, "integer"))
