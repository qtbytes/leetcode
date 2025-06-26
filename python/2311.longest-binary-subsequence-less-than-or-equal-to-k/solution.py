# Created by none at 2025/06/26 11:03
# leetgo: dev
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

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
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        nums = list(map(int, s))

        # we must choose all 0
        # because 0 is always better than 1

        res = nums.count(0)

        x = 0
        for i in range(n - 1, -1, -1):
            x |= nums[i] << (n - 1 - i)
            if x > k:
                break
            res += nums[i]

        return res

        # Solution of SubStr

        # x = 0
        # res = 0
        # l = 0

        # nums = list(map(int, s))

        # for r, y in enumerate(nums):
        #     x = (x << 1) | y
        #     while x > k:
        #         x -= nums[l] << (r - l)
        #         l += 1
        #     res = max(res, r - l + 1)
        # return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestSubsequence(s, k)
    print("\noutput:", serialize(ans, "integer"))
