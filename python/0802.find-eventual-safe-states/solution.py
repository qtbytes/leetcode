# Created by none at 2025/01/24 09:28
# leetgo: 1.4.13
# https://leetcode.com/problems/find-eventual-safe-states/

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
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        n = len(g)
        f = [-1] * n

        def dfs(x: int):
            f[x] = 0
            for y in g[x]:
                if (f[y] == -1 and dfs(y) == 0) or f[y] == 0:
                    return 0
            f[x] = 1
            return f[x]

        res = []
        for i in range(n):
            if f[i] == -1:
                dfs(i)
            if f[i] == 1:
                res.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eventualSafeNodes(graph)
    print("\noutput:", serialize(ans, "integer[]"))
