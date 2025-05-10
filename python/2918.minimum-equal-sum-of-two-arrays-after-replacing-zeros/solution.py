# Created by none at 2025/05/10 21:57
# leetgo: 1.4.13
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

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
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def f(nums: list[int]):
            """return sum and count of zero"""
            sum = zero = 0
            for x in nums:
                sum += x
                if x == 0:
                    zero += 1
            return sum, zero

        s1, z1 = f(nums1)
        s2, z2 = f(nums2)

        if z1 == 0 and s1 < s2 + z2 or z2 == 0 and s2 < s1 + z1:
            return -1
        return max(s1 + z1, s2 + z2)


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSum(nums1, nums2)
    print("\noutput:", serialize(ans, "long"))
