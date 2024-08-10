# Created by none at 2024/08/10 14:02
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/

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
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(queries)
        q = sorted(zip(queries, range(n)), key=lambda e: max(e[0]), reverse=True)

        res = [-1] * n

        can = collections.deque()
        j = len(heights) - 1

        for (x, y), _i in q:
            x, y = sorted([x, y])
            if x == y or heights[x] < heights[y]:
                res[_i] = y
                continue
            i = max(x, y)  # add [i..] to can
            while j >= i:
                # add heights[j]
                while can and heights[j] >= heights[can[0]]:
                    can.popleft()
                can.appendleft(j)
                j -= 1
            h = max(heights[x], heights[y])  # find the leftmost can[_j] > h

            ans = bisect.bisect_left(can, h + 1, key=lambda _j: heights[_j])
            if ans < len(can):
                res[_i] = can[ans]
        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().leftmostBuildingQueries(heights, queries)
    print("\noutput:", serialize(ans, "integer[]"))
