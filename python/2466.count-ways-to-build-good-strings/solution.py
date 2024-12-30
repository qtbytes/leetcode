# Created by none at 2024/12/30 15:59
# leetgo: 1.4.11
# https://leetcode.com/problems/count-ways-to-build-good-strings/

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
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        @cache
        def dfs(i: int, n: int):
            if i > n:
                return 0
            res = 1 + dfs(i + zero, n) + dfs(i + one, n)
            return res % mod

        res = dfs(0, high) - dfs(0, low - 1)
        return res % mod


# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    zero: int = deserialize("int", read_line())
    one: int = deserialize("int", read_line())
    ans = Solution().countGoodStrings(low, high, zero, one)
    print("\noutput:", serialize(ans, "integer"))
