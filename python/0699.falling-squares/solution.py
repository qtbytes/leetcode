# Created by none at 2024/07/28 12:12
# leetgo: 1.4.7
# https://leetcode.cn/problems/falling-squares/

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
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        when (x, L) drop
        we should find max_height(x, x + L) and set range(x, x + L+1) to h + L
        """
        # map x to index [1,1000]
        x_points = []
        for x, L in positions:
            x_points.append(x)
            x_points.append(x + L)

        mp = {v: i for i, v in enumerate(sorted(set(x_points)))}
        n = len(mp)

        height = [0] * n

        def max_height(l, r):
            if r > n:
                r = n
            res = 0
            for h in range(l, r):
                if height[h] > res:
                    res = height[h]
            return res

        res = []

        def set_height(l, r, h):
            if r > n:
                r = n
            for x in range(l, r):
                height[x] = h

        cur = 0
        for _x, L in positions:
            l = mp[_x]
            r = mp[_x + L]

            h = max_height(l, r) + L
            if h > cur:
                cur = h
            set_height(l, r, h)
            res.append(cur)

        return res


# @lc code=end

if __name__ == "__main__":
    positions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().fallingSquares(positions)
    print("\noutput:", serialize(ans, "integer[]"))
