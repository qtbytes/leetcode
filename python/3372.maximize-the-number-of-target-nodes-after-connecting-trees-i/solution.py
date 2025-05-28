# Created by none at 2025/05/28 10:16
# leetgo: dev
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

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
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        def build_edge(edge: list[list[int]]):
            g = [[] for _ in range(len(edge) + 1)]

            for x, y in edge:
                g[x].append(y)
                g[y].append(x)

            return g

        def dfs(g: list[list[int]], x: int, fa: int, k: int):
            if k < 0:
                return 0
            res = 1
            for y in g[x]:
                if y == fa:
                    continue
                res += dfs(g, y, x, k - 1)
            return res

        g = build_edge(edges2)
        # find the node with max score of (k-1)
        extra_score = max(dfs(g, x, -1, k - 1) for x in range(len(edges2) + 1))
        g = build_edge(edges1)
        return [dfs(g, x, -1, k) + extra_score for x in range(len(edges1) + 1)]


# @lc code=end

if __name__ == "__main__":
    edges1: List[List[int]] = deserialize("List[List[int]]", read_line())
    edges2: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxTargetNodes(edges1, edges2, k)
    print("\noutput:", serialize(ans, "integer[]"))
