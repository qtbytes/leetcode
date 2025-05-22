# Created by none at 2025/05/22 11:51
# leetgo: dev
# https://leetcode.com/problems/zero-array-transformation-iii/

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
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)
        queries.sort()
        m, j = len(queries), 0
        d = 0
        q = []
        for i, x in enumerate(nums):
            while j < m and queries[j][0] <= i:
                heappush(q, -queries[j][1])
                j += 1
            d += diff[i]
            while d < x and q and -q[0] >= i:
                d += 1
                diff[-heappop(q) + 1] -= 1
            if d < x:
                return -1
        return len(q)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxRemoval(nums, queries)
    print("\noutput:", serialize(ans, "integer"))
