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
INF = -(10**9)


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[INF] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][2] = 0
        for i, p in enumerate(prices, 1):
            dp[i][0][2] = 0
            for j in range(1, k + 1):
                dp[i][j][2] = max(
                    dp[i - 1][j][2], p + dp[i - 1][j][1], -p + dp[i - 1][j][0]
                )
                dp[i][j][1] = max(dp[i - 1][j][1], -p + dp[i - 1][j - 1][2])
                dp[i][j][0] = max(dp[i - 1][j][0], p + dp[i - 1][j - 1][2])
        return max(dp[-1][j][2] for j in range(1, k + 1))


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumProfit(prices, k)
    print("\noutput:", serialize(ans, "long"))
