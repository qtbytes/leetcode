# Created by none at 2025/06/09 11:53
# leetgo: dev
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

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


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def find(n: int, x: int):
            """count how many number start with x and less than n"""
            # n = 456, x=1
            # 1, 10..19, 100..199
            # 2, 20..29
            d = 1
            res = 0
            while x * d <= n:
                res += min(n, x * d + d - 1) - x * d + 1
                d *= 10
            return res

        k -= 1
        res = 1
        while k > 0:
            cnt = find(n, res)
            if cnt <= k:
                res += 1
                k -= cnt
            else:
                res *= 10
                k -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthNumber(n, k)
    print("\noutput:", serialize(ans, "integer"))
