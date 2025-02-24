# Created by none at 2025/02/24 14:18
# leetgo: 1.4.13
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

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
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        next = {}

        def find_bob(x: int, fa: int) -> bool:
            if x == bob:
                return True
            for y in g[x]:
                if y == fa:
                    continue
                if find_bob(y, x):
                    next[x] = y
                    return True
            return False

        is_leaf = [False] * n

        def find_leaf(x: int, fa: int):
            size = 1
            for y in g[x]:
                if y == fa:
                    continue
                size += find_leaf(y, x)
            if size == 1:
                is_leaf[x] = True
            return size

        def dfs(x: int, fa: int, cnt: int):
            res = -inf
            for y in g[x]:
                if y == fa:
                    continue
                # path move to bob
                if x in next and y == next[x]:
                    #  meet at middle
                    if len(next) & 1 == 0 and cnt + 1 == len(next) // 2:
                        res = max(res, amount[y] // 2 + dfs(y, x, cnt + 1))
                    elif cnt + 1 <= len(next) // 2:
                        res = max(res, amount[y] + dfs(y, x, cnt + 1))
                    else:
                        res = max(res, dfs(y, x, cnt + 1))
                else:
                    res = max(res, amount[y] + dfs(y, x, cnt))
            return 0 if is_leaf[x] else res

        find_bob(0, -1)
        find_leaf(0, -1)
        return amount[0] + dfs(0, -1, 0)


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    bob: int = deserialize("int", read_line())
    amount: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostProfitablePath(edges, bob, amount)
    print("\noutput:", serialize(ans, "integer"))
