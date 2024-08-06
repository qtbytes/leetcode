# Created by none at 2024/08/06 14:39
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/

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
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        - `1 <= zero, one, limit <= 200`
        """
        mod = 10**9 + 7

        @functools.cache
        def dfs(i: int, j: int, num: int):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            res = 0

            if num == 1:  # need 1
                if i == 0:
                    return 0
                for k in range(1, min(i, limit) + 1):
                    res += dfs(i - k, j, num ^ 1)
            else:
                if j == 0:
                    return 0
                for k in range(1, min(j, limit) + 1):
                    res += dfs(i, j - k, num ^ 1)

            return res % mod

        return (dfs(one, zero, 1) + dfs(one, zero, 0)) % mod

        # a, b = sorted([zero, one], reverse=True)
        # limit += 1
        # total = math.comb(a + b, b) % mod
        # if a >= limit:
        #     one = math.comb(a - limit + 1 + b, b) % mod
        # else:
        #     return total
        # if b >= limit:
        #     zero = math.comb(a - limit + 1 + b, a) % mod
        #     both = math.comb(a - limit + 1 + b - limit + 1, a - limit + 1) % mod
        #     return (total - one - zero + both) % mod
        # print(total, one)
        # return (total - one) % mod


# @lc code=end

if __name__ == "__main__":
    zero: int = deserialize("int", read_line())
    one: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numberOfStableArrays(zero, one, limit)
    print("\noutput:", serialize(ans, "integer"))
