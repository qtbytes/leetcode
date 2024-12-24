# Created by none at 2024/12/24 15:12
# leetgo: 1.4.11
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

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
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # we want a minimal tree, and the first and second longest edge

        def longest(edges: list[list[int]]):
            n = len(edges) + 1
            deg = [0] * n
            g = [[] for _ in range(n)]
            for x, y in edges:
                deg[x] += 1
                deg[y] += 1
                g[x].append(y)
                g[y].append(x)

            q = deque()
            for i, d in enumerate(deg):
                if d == 1:
                    q.append(i)

            if not q:
                return 0, 0

            cnt = 0
            while q and n > 2:
                size = len(q)
                n -= size
                cnt += 1
                for _ in range(size):
                    x = q.popleft()
                    for y in g[x]:
                        deg[y] -= 1
                        if deg[y] == 1:
                            q.append(y)

            if n == 2:
                return cnt + 1, cnt
            return cnt, cnt

        f1, s1 = longest(edges1)
        f2, s2 = longest(edges2)

        return max(f1 + max(s1, f2 + 1), f2 + max(f1 + 1, s2))


# @lc code=end

if __name__ == "__main__":
    edges1: List[List[int]] = deserialize("List[List[int]]", read_line())
    edges2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumDiameterAfterMerge(edges1, edges2)
    print("\noutput:", serialize(ans, "integer"))
