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

        def dp(g: list[list[int]]):
            f = [[0] * 2 for _ in range(len(g))]

            def dfs(x: int, fa: int):
                op0, op1 = 1, 0
                for y in g[x]:
                    if y == fa:
                        continue
                    sub0, sub1 = dfs(y, x)
                    op0 += sub1
                    op1 += sub0
                f[x] = [op0, op1]
                return op0, op1

            def change_root(x: int, fa: int):
                for y in g[x]:
                    if y == fa:
                        continue
                    op0, op1 = f[x]
                    op0 -= f[y][1]
                    op1 -= f[y][0]
                    f[y][1] += op0
                    f[y][0] += op1
                    change_root(y, x)

            dfs(0, -1)
            change_root(0, -1)
            return f

        extra = max(op1 for _, op1 in dp(build_edges(edges2)))
        return [op0 + extra for op0, _ in dp(build_edges(edges1))]


# @lc code=end

if __name__ == "__main__":
    edges1: List[List[int]] = deserialize("List[List[int]]", read_line())
    edges2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTargetNodes(edges1, edges2)
    print("\noutput:", serialize(ans, "integer[]"))
