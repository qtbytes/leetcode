# Created by none at 2025/05/23 16:00
# leetgo: dev
# https://leetcode.com/problems/optimal-account-balancing/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin
N = 12


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = [0] * N
        for _from, to, x in transactions:
            balance[_from] -= x
            balance[to] += x

        n = len(balance)

        def dfs(i: int) -> int:
            if i == n:
                return 0
            if balance[i] == 0:
                return dfs(i + 1)
            res = inf
            for j in range(i + 1, n):
                if balance[i] * balance[j] < 0:
                    balance[j] += balance[i]
                    res = min(res, 1 + dfs(i + 1))
                    balance[j] -= balance[i]
            return res

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    transactions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTransfers(transactions)
    print("\noutput:", serialize(ans, "integer"))
