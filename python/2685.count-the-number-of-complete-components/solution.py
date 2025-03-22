# Created by none at 2025/03/22 14:39
# leetgo: 1.4.13
# https://leetcode.com/problems/count-the-number-of-complete-components/

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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        res = 0
        visited = [False] * n
        for x in range(n):
            if visited[x]:
                continue

            # BFS
            q = [x]
            nodes = [x]
            visited[x] = True
            size = 1
            while q:
                next = []
                for x in q:
                    for y in g[x]:
                        if not visited[y]:
                            size += 1
                            visited[y] = True
                            next.append(y)
                            nodes.append(y)
                q = next

            # print(nodes, size, g)
            res += all(len(g[x]) == size - 1 for x in nodes)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countCompleteComponents(n, edges)
    print("\noutput:", serialize(ans, "integer"))
