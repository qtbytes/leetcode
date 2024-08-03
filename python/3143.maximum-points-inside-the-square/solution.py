# Created by none at 2024/08/03 12:22
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-points-inside-the-square/

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
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        q = [(max(abs(x) for x in e), tag) for e, tag in zip(points, s)]
        q.sort()

        seen = set()
        res = 0
        i = 0
        n = len(q)
        while i < n:
            if q[i][1] in seen:
                return res
            seen.add(q[i][1])
            j = i + 1
            while j < n and q[j][0] == q[j - 1][0]:
                if q[j][1] in seen:
                    return res
                seen.add(q[j][1])
                j += 1
            res += j - i
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().maxPointsInsideSquare(points, s)
    print("\noutput:", serialize(ans, "integer"))
