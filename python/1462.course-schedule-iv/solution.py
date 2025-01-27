# Created by none at 2025/01/27 11:01
# leetgo: 1.4.13
# https://leetcode.com/problems/course-schedule-iv/

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
    def checkIfPrerequisite(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)

        @cache
        def dfs(x: int, target: int) -> bool:
            for y in g[x]:
                if y == target or dfs(y, target):
                    return True
            return False

        return [dfs(x, y) for x, y in queries]

        # fa = list(range(numCourses))
        # size = [1] * numCourses

        # def find(x: int):
        #     if fa[x] != x:
        #         fa[x] = find(fa[x])
        #     return fa[x]

        # def union(x: int, y: int):
        #     fx, fy = find(x), find(y)
        #     size[fx] += size[fy]
        #     fa[fy] = fx

        # for x, y in prerequisites:
        #     union(x, y)

        # res = []
        # for x, y in queries:
        #     fx, fy = find(x), find(y)
        #     print(fx, fy)
        #     res.append(fx == fy and size[x] > size[y])
        # return res


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkIfPrerequisite(numCourses, prerequisites, queries)
    print("\noutput:", serialize(ans, "boolean[]"))
