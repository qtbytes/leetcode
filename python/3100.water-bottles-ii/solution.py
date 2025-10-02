# Created by none at 2025/10/02 14:22
# leetgo: dev
# https://leetcode.com/problems/water-bottles-ii/

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
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles -= numExchange - 1
            numExchange += 1
        return res + numBottles


# @lc code=end

if __name__ == "__main__":
    numBottles: int = deserialize("int", read_line())
    numExchange: int = deserialize("int", read_line())
    ans = Solution().maxBottlesDrunk(numBottles, numExchange)
    print("\noutput:", serialize(ans, "integer"))
