# Created by none at 2024/08/15 12:40
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-difference-score-in-a-grid/

import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import string
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int | float:
        m, n = len(grid), len(grid[0])
        res = -math.inf
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                x = grid[i][j]
                if i + 1 < m:
                    grid[i][j] = max(grid[i][j], grid[i + 1][j])
                    res = max(res, grid[i + 1][j] - x)
                if j + 1 < n:
                    grid[i][j] = max(grid[i][j], grid[i][j + 1])
                    res = max(res, grid[i][j + 1] - x)
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxScore(grid)
    print("\noutput:", serialize(ans, "integer"))
