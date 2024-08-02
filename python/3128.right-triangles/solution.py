# Created by none at 2024/08/02 12:17
# leetgo: 1.4.7
# https://leetcode.cn/problems/right-triangles/

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
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    res += (rows[i] - 1) * (cols[j] - 1)
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfRightTriangles(grid)
    print("\noutput:", serialize(ans, "long"))
