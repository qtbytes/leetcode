# Created by none at 2025/05/08 11:58
# leetgo: 1.4.13
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import *
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int | float:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = [(0, 0, 0, 0)]  # (dist, x, y, extra_time)

        while q:
            d, x, y, extra = heappop(q)
            for dx, dy in pairwise((0, 1, 0, -1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == inf:
                    dist[nx][ny] = max(d, moveTime[nx][ny]) + (1 + extra)
                    heappush(q, (dist[nx][ny], nx, ny, extra ^ 1))

        return dist[-1][-1]


# @lc code=end

if __name__ == "__main__":
    moveTime: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTimeToReach(moveTime)
    print("\noutput:", serialize(ans, "integer"))
