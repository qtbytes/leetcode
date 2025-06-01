# Created by none at 2025/06/01 23:33
# leetgo: dev
# https://leetcode.com/problems/distribute-candies-among-children-ii/

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
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0

        res = 0
        for first in range(max(0, n - 2 * limit), min(n, limit) + 1):
            rest = n - first
            if rest <= limit:
                res += rest + 1
            else:
                res += limit - (rest - limit) + 1

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(n, limit)
    print("\noutput:", serialize(ans, "long"))
