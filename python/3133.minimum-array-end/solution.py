# Created by none at 2024/08/22 14:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-array-end/

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
    def minEnd(self, n: int, x: int) -> int:
        N = 60
        n -= 1
        for i in range(N):
            if x >> i & 1:
                continue
            if n & 1:
                x |= 1 << i
            n >>= 1
            if n == 0:
                break
        return x


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minEnd(n, x)
    print("\noutput:", serialize(ans, "long"))
