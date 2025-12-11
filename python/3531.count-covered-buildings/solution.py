# Created by none at 2025/12/11 12:47
# leetgo: dev
# https://leetcode.com/problems/count-covered-buildings/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = [[] for _ in range(n + 1)]
        cols = [[] for _ in range(n + 1)]

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        for row in rows:
            row.sort()
        for col in cols:
            col.sort()

        res = 0
        for x, y in buildings:
            i = bisect_left(rows[x], y)
            j = bisect_left(cols[y], x)
            if 0 < i < len(rows[x]) - 1 and 0 < j < len(cols[y]) - 1:
                res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    buildings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countCoveredBuildings(n, buildings)
    print("\noutput:", serialize(ans, "integer"))
