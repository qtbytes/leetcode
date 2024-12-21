# Created by none at 2024/12/21 14:15
# leetgo: 1.4.11
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

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
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        res = 0

        def dfs(x: int, fa: int):
            score = values[x]
            for y in g[x]:
                if y != fa:
                    score += dfs(y, x)
            # remove edge(fa, x)
            if score % k == 0:
                nonlocal res
                res += 1
            return score % k

        dfs(0, -1)

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    values: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxKDivisibleComponents(n, edges, values, k)
    print("\noutput:", serialize(ans, "integer"))
