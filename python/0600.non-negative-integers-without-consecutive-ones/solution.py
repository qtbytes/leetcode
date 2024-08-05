# Created by none at 2024/08/05 11:58
# leetgo: 1.4.7
# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/

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
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]
        size = len(s)

        @functools.cache
        def dp(i: int, is_num: bool, limit: bool, one: bool):
            if i == size:
                return 1
            res = 0
            up = 1 if not limit else int(s[i])
            for d in range(up + 1):
                if not (d == 1 and one):
                    res += dp(i + 1, d == 1 or is_num, limit and d == up, d == 1)
            return res

        return dp(0, False, True, False)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().findIntegers(n)
    print("\noutput:", serialize(ans, "integer"))
