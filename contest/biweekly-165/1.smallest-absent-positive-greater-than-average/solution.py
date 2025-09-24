# Created by none at 2025/09/23 22:36
# leetgo: dev
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/
# https://leetcode.com/contest/biweekly-contest-165/problems/smallest-absent-positive-greater-than-average/

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
    def smallestAbsent(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        nums_set = set(nums)
        for x in count(1):
            if x not in nums_set and x * n > s:
                return x
        return -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestAbsent(nums)
    print("\noutput:", serialize(ans, "integer"))
