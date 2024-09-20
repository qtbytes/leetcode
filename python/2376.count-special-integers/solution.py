# Created by none at 2024/09/20 13:11
# leetgo: 1.4.9
# https://leetcode.cn/problems/count-special-integers/

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
    def countSpecialNumbers(self, x: int) -> int:
        s = str(x)
        n = len(s)

        @functools.cache
        def dfs(i: int, mask: int, limit: bool, is_num: bool):
            if i == n:
                return 1
            res = 0
            if not is_num:
                res += dfs(i + 1, mask, False, is_num)

            low = 1 if not is_num else 0
            up = 9 if not limit else int(s[i])
            for d in range(low, up + 1):
                if mask >> d & 1 == 0:
                    res += dfs(
                        i + 1, mask | (1 << d), limit and d == up, is_num or d > 0
                    )
            return res

        return dfs(0, 0, True, False) - 1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countSpecialNumbers(n)
    print("\noutput:", serialize(ans, "integer"))
