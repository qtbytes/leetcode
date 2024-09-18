# Created by none at 2024/09/18 11:40
# leetgo: 1.4.9
# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/

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
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        """
        - `n == buses.length`
        - `m == passengers.length`
        - `1 <= n, m, capacity <= 10⁵`
        - `2 <= buses[i], passengers[i] <= 10⁹`
        - Each element in `buses` is **unique**.
        - Each element in `passengers` is **unique**.
        """
        buses.sort()
        passengers.sort()

        n, i = len(passengers), 0

        K = capacity

        # use the [0:m-1] buses
        m = len(buses)
        for j in range(m - 1):
            t = buses[j]
            capacity = K
            while capacity > 0 and i < n and passengers[i] <= t:
                capacity -= 1
                i += 1

        # the last bus
        t = buses[m - 1]
        capacity = K
        while capacity > 1 and i < n and passengers[i] <= t:
            capacity -= 1
            i += 1

        res = t
        if i < n:
            res = min(res, passengers[i] - 1)
        while i > 0 and res == passengers[i - 1]:
            res -= 1
            i -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    buses: List[int] = deserialize("List[int]", read_line())
    passengers: List[int] = deserialize("List[int]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().latestTimeCatchTheBus(buses, passengers, capacity)
    print("\noutput:", serialize(ans, "integer"))
