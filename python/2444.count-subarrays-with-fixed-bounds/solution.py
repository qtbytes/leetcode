# Created by none at 2025/04/26 11:35
# leetgo: 1.4.13
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

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
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_valid = -1
        last_min = -1
        last_max = -1

        res = 0
        for i, x in enumerate(nums):
            if x == maxK:
                last_max = i
            if x == minK:
                last_min = i
            if not (minK <= x <= maxK):
                last_valid = i
            res += max(0, min(last_max, last_min) - last_valid)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    minK: int = deserialize("int", read_line())
    maxK: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, minK, maxK)
    print("\noutput:", serialize(ans, "long"))
