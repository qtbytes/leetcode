# Created by none at 2025/03/20 10:50
# leetgo: 1.4.13
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

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
    def minimumCost(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        fa = list(range(n))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            fa[fy] = fx
            return True

        for x, y, _ in edges:
            union(x, y)

        group = [-1] * n  # & all connected nodes whose fa is group[i]
        for x, y, w in edges:
            group[find(x)] &= w

        res = []
        for x, y in query:
            fx, fy = find(x), find(y)
            if fx != fy:
                res.append(-1)
            else:
                res.append(group[fx])
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    query: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumCost(n, edges, query)
    print("\noutput:", serialize(ans, "integer[]"))
