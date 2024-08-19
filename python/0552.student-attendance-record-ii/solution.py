# Created by none at 2024/08/19 11:21
# leetgo: 1.4.7
# https://leetcode.cn/problems/student-attendance-record-ii/

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
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7

        @functools.cache
        def dfs(n: int, a: int, l: int):
            if n == 0:
                return 1
            res = 0
            if a < 1:
                res += dfs(n - 1, a + 1, 0)
            if l < 2:
                res += dfs(n - 1, a, l + 1)
            res += dfs(n - 1, a, 0)

            return res % mod

        res = dfs(n, 0, 0)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().checkRecord(n)
    print("\noutput:", serialize(ans, "integer"))
