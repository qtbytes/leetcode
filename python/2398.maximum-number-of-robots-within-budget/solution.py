# Created by none at 2024/09/13 20:54
# leetgo: 1.4.9
# https://leetcode.cn/problems/maximum-number-of-robots-within-budget/

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
    def maximumRobots(
        self, chargeTimes: List[int], runningCosts: List[int], budget: int
    ) -> int:
        """
        - `chargeTimes.length == runningCosts.length == n`
        - `1 <= n <= 5 * 10⁴`
        - `1 <= chargeTimes[i], runningCosts[i] <= 10⁵`
        - `1 <= budget <= 10¹⁵`
        """
        p = list(itertools.accumulate(runningCosts, initial=0))

        n = len(runningCosts)

        def check(mid):
            q = []  # maintain the max for range(i,i+mid)
            for i in range(mid - 1):
                heapq.heappush(q, (-chargeTimes[i], i))
            for i in range(mid - 1, n):
                while q and q[0][1] + mid <= i:
                    heapq.heappop(q)
                heapq.heappush(q, (-chargeTimes[i], i))
                cur = -q[0][0] + mid * (p[i + 1] - p[i - (mid - 1)])
                if cur <= budget:
                    return True
            return False

        l = 0
        r = n

        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return r


# @lc code=end

if __name__ == "__main__":
    chargeTimes: List[int] = deserialize("List[int]", read_line())
    runningCosts: List[int] = deserialize("List[int]", read_line())
    budget: int = deserialize("int", read_line())
    ans = Solution().maximumRobots(chargeTimes, runningCosts, budget)
    print("\noutput:", serialize(ans, "integer"))
