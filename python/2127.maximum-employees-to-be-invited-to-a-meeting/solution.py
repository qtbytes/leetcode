# Created by none at 2025/01/26 13:43
# leetgo: 1.4.13
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

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
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        for x, y in enumerate(favorite):
            deg[y] += 1
        q = deque([i for i, d in enumerate(deg) if d == 0])
        extra = [0] * n
        visited = [False] * n
        # extra link
        while q:
            x = q.popleft()
            visited[x] = True
            y = favorite[x]
            extra[y] = max(extra[y], extra[x] + 1)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        res = 0
        circle_with_link = 0

        for x in range(n):
            if visited[x]:
                continue
            # calculate circle size
            circle_size = 0
            while not visited[x]:
                circle_size += 1
                visited[x] = True
                x = favorite[x]
            # O -> O -> O <-> O <- O
            if circle_size == 2:
                circle_with_link += 2 + extra[x] + extra[favorite[x]]
            else:
                res = max(res, circle_size)

        return max(res, circle_with_link)


# @lc code=end

if __name__ == "__main__":
    favorite: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumInvitations(favorite)
    print("\noutput:", serialize(ans, "integer"))
