# Created by none at 2025/05/29 12:49
# leetgo: dev
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

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
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def build_edges(edge: list[list[int]]):
            g = [[] for _ in range(len(edge) + 1)]
            for x, y in edge:
                g[x].append(y)
                g[y].append(x)
            return g

        g = build_edges(edges2)
        cnt = [0] * 2

        def dfs(x: int, fa: int, color: int):
            cnt[color] += 1
            for y in g[x]:
                if y == fa:
                    continue
                dfs(y, x, color ^ 1)

        dfs(0, -1, 0)
        extra = max(cnt)

        g = build_edges(edges1)
        cnt = [0] * 2
        res = [extra] * len(g)
        dfs(0, -1, 0)

        def change_root(x: int, fa: int, color: int):
            res[x] += cnt[color]
            for y in g[x]:
                if y == fa:
                    continue
                change_root(y, x, color ^ 1)

        change_root(0, -1, 0)
        return res


# @lc code=end

if __name__ == "__main__":
    edges1: List[List[int]] = deserialize("List[List[int]]", read_line())
    edges2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTargetNodes(edges1, edges2)
    print("\noutput:", serialize(ans, "integer[]"))
