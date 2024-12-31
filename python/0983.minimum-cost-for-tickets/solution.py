# Created by none at 2024/12/31 14:04
# leetgo: 1.4.11
# https://leetcode.com/problems/minimum-cost-for-tickets/

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
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        ticket = [1, 7, 30]

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0
            res = inf
            for j, cost in enumerate(costs):
                k = bisect_left(days, days[i] + ticket[j])
                res = min(res, cost + dfs(k))
            return res

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    days: List[int] = deserialize("List[int]", read_line())
    costs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mincostTickets(days, costs)
    print("\noutput:", serialize(ans, "integer"))
