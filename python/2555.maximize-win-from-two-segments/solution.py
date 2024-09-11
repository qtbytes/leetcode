# Created by none at 2024/09/11 10:53
# leetgo: 1.4.9
# https://leetcode.cn/problems/maximize-win-from-two-segments/

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
    def maximizeWin(self, p: List[int], k: int) -> int:
        res = 0
        n = len(p)
        f = [0] * (n + 1)
        l = 0

        for r, x in enumerate(p):
            while x - p[l] > k:
                l += 1
            res = max(res, r - l + 1 + f[l - 1])
            f[r] = max(f[r - 1], r - l + 1)

        return res


# @lc code=end

if __name__ == "__main__":
    prizePositions: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximizeWin(prizePositions, k)
    print("\noutput:", serialize(ans, "integer"))
