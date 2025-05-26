# Created by none at 2025/05/26 10:04
# leetgo: dev
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

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
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            if x == y:  # circle
                return -1
            g[x].append(y)
            deg[y] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)

        colors = list(ord(ch) - ord("a") for ch in colors)

        def check_color(color: str, q: deque[int], deg: list[int]) -> int:
            f = [0] * n
            rest_node = n - len(q)
            while q:
                x = q.popleft()
                if colors[x] == color:
                    f[x] += 1
                for y in g[x]:
                    deg[y] -= 1
                    f[y] = max(f[y], f[x])
                    if deg[y] == 0:
                        rest_node -= 1
                        q.append(y)
            if rest_node:
                return inf
            return max(f)

        res = max(check_color(color, q.copy(), deg.copy()) for color in set(colors))
        return -1 if res == inf else res

        # f = [[0] * 26 for _ in range(n)]
        # rest_node = n - len(q)
        # res = 0
        # while q:
        #     x = q.popleft()
        #     f[x][colors[x]] += 1
        #     res = max(res, f[x][colors[x]])
        #     for y in g[x]:
        #         deg[y] -= 1
        #         for c in range(26):
        #             f[y][c] = max(f[y][c], f[x][c])
        #         if deg[y] == 0:
        #             rest_node -= 1
        #             q.append(y)
        # return -1 if rest_node else res


# @lc code=end

if __name__ == "__main__":
    colors: str = deserialize("str", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestPathValue(colors, edges)
    print("\noutput:", serialize(ans, "integer"))
