# Created by none at 2025/06/03 13:02
# leetgo: dev
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        res = 0
        n = len(status)
        q = deque()
        for box in initialBoxes:
            if status[box] == 1:
                q.appendleft(box)
            else:
                q.append(box)

        visited = [False] * n
        while q:
            x = q.popleft()
            if visited[x] or status[x] == 0:
                continue
            visited[x] = True
            res += candies[x]
            for box in keys[x]:
                status[box] = 1
            keys[x].clear()
            for box in containedBoxes[x]:
                if status[box] == 1:
                    q.appendleft(box)
                else:
                    q.append(box)
        return res


# @lc code=end

if __name__ == "__main__":
    status: List[int] = deserialize("List[int]", read_line())
    candies: List[int] = deserialize("List[int]", read_line())
    keys: List[List[int]] = deserialize("List[List[int]]", read_line())
    containedBoxes: List[List[int]] = deserialize("List[List[int]]", read_line())
    initialBoxes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print("\noutput:", serialize(ans, "integer"))
