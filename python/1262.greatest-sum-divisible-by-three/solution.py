# Created by none at 2025/11/23 12:12
# leetgo: dev
# https://leetcode.com/problems/greatest-sum-divisible-by-three/

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
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        g = [[] for _ in range(3)]
        for x in nums:
            g[x % 3].append(x)
        for v in g:
            v.sort()
        res = 0
        match s % 3:
            case 0:
                res = s
            case 1:
                # remove one 1 or two 2
                if g[1]:
                    res = s - g[1][0]
                if len(g[2]) >= 2:
                    res = max(res, s - sum(g[2][:2]))
            case 2:
                # remove two 1 or one 2
                if g[2]:
                    res = s - g[2][0]
                if len(g[1]) >= 2:
                    res = max(res, s - sum(g[1][:2]))
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumDivThree(nums)
    print("\noutput:", serialize(ans, "integer"))
