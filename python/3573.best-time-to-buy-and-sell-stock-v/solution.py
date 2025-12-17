# Created by none at 2025/12/17 10:47
# leetgo: dev
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

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
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, state: int, k: int) -> int:
            if i == n:
                return 0 if state == 0 else -(10**9)
            res = dfs(i + 1, state, k)
            if state == 1:
                res = max(res, prices[i] + dfs(i + 1, 0, k))
            elif state == -1:
                res = max(res, -prices[i] + dfs(i + 1, 0, k))
            elif k > 0:
                res = max(
                    res,
                    -prices[i] + dfs(i + 1, 1, k - 1),
                    prices[i] + dfs(i + 1, -1, k - 1),
                )
            return res

        res = dfs(0, 0, k)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumProfit(prices, k)
    print("\noutput:", serialize(ans, "long"))
