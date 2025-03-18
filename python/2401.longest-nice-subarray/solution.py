# Created by none at 2025/03/18 10:41
# leetgo: 1.4.13
# https://leetcode.com/problems/longest-nice-subarray/

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
N = 31


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        # cnt = [0] * N
        mask = 0
        for r, x in enumerate(nums):
            while mask & x != 0:
                mask ^= nums[l]  # remove left
                l += 1
            mask |= x
            res = max(res, r - l + 1)
            # ok = True
            # for i in range(N):
            #     if x >> i & 1:
            #         cnt[i] += 1
            #         if cnt[i] > 1:
            #             ok = False
            # while not ok:
            #     x = nums[l]
            #     ok = True
            #     for i in range(N):
            #         if x >> i & 1:
            #             cnt[i] -= 1
            #         if cnt[i] > 1:
            #             ok = False
            #     l += 1
            # res = max(res, r - l + 1)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestNiceSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
