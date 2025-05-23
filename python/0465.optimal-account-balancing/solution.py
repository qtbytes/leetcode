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

        pos = []
        neg = []
        for x in balance:
            if x < 0:
                neg.append(-x)
            elif x > 0:
                pos.append(x)

        m, n = len(pos), len(neg)

        def dfs(i: int) -> int:
            if i == m:
                return 0
            if pos[i] == 0:
                return dfs(i + 1)
            res = inf
            for j in range(n):
                if neg[j] != 0:
                    value = min(neg[j], pos[i])
                    pos[i] -= value
                    neg[j] -= value

                    res = min(res, 1 + dfs(i))

                    pos[i] += value
                    neg[j] += value
            return res

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    transactions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minTransfers(transactions)
    print("\noutput:", serialize(ans, "integer"))
