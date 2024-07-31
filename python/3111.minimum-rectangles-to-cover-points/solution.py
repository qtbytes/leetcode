# Created by none at 2024/07/31 09:31
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-rectangles-to-cover-points/

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
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        q = sorted(set(x for x, _ in points))
        i = 0
        n = len(q)
        res = 0
        while i < n:
            j = i
            while j < n and q[j] - q[i] <= w:
                j += 1
            res += 1
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    w: int = deserialize("int", read_line())
    ans = Solution().minRectanglesToCoverPoints(points, w)
    print("\noutput:", serialize(ans, "integer"))
