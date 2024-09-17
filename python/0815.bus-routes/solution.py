# Created by none at 2024/09/17 14:48
# leetgo: 1.4.9
# https://leetcode.cn/problems/bus-routes/

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
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        """
        - `1 <= routes.length <= 500`.
        - `1 <= routes[i].length <= 10⁵`
        - All the values of `routes[i]` are **unique**.
        - `sum(routes[i].length) <= 10⁵`
        - `0 <= routes[i][j] < 10⁶`
        - `0 <= source, target < 10⁶`
        """
        if source == target:
            return 0

        mp = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                mp[stop].append(i)

        q = collections.deque()
        for route in mp[source]:
            q.append((1, route))

        while q:
            route_cnt, route_i = q.popleft()
            for stop in routes[route_i]:
                if stop == target:
                    return route_cnt
                for route_j in mp[stop]:
                    q.append((route_cnt + 1, route_j))
                del mp[stop]
            routes[route_i].clear()

        return -1


# @lc code=end

if __name__ == "__main__":
    routes: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numBusesToDestination(routes, source, target)
    print("\noutput:", serialize(ans, "integer"))
