# Created by none at 2025/12/14 12:39
# leetgo: dev
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

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
mod = 10**9 + 7


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        index = [i for i, ch in enumerate(corridor) if ch == "S"]
        n = len(index)
        if n & 1 == 1 or n == 0:
            return 0
        res = 1
        for i in range(2, n, 2):
            res = (res * (index[i] - index[i - 1])) % mod
        return res


# @lc code=end

if __name__ == "__main__":
    corridor: str = deserialize("str", read_line())
    ans = Solution().numberOfWays(corridor)
    print("\noutput:", serialize(ans, "integer"))
