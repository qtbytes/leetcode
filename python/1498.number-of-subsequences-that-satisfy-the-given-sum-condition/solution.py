# Created by none at 2025/06/29 14:02
# leetgo: dev
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

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
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        l, r = 0, n - 1
        while l <= r:
            # we try to use nums[l] as minimal
            while r >= l and nums[l] + nums[r] > target:
                r -= 1
            if l <= r:
                res += pow(2, r - l, mod)
            l += 1
        return res % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numSubseq(nums, target)
    print("\noutput:", serialize(ans, "integer"))
