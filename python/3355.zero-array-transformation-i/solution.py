# Created by none at 2025/05/20 10:55
# leetgo: dev
# https://leetcode.com/problems/zero-array-transformation-i/

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
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for start, end in queries:
            diff[start] -= 1
            diff[end + 1] += 1

        sum = 0
        for x, d in zip(nums, diff):
            sum += d
            if x + sum > 0:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isZeroArray(nums, queries)
    print("\noutput:", serialize(ans, "boolean"))
