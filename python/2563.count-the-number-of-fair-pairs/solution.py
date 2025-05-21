# Created by none at 2025/04/19 16:30
# leetgo: 1.4.13
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

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
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i, x in enumerate(nums):
            l = bisect_left(nums, lower - x, lo=i + 1)
            r = bisect_right(nums, upper - x, lo=i + 1)
            res += r - l
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().countFairPairs(nums, lower, upper)
    print("\noutput:", serialize(ans, "long"))
