# Created by none at 2025/09/23 22:36
# leetgo: dev
# https://leetcode.com/problems/maximum-xor-of-subsequences/
# https://leetcode.com/contest/biweekly-contest-165/problems/maximum-xor-of-subsequences/

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
    def maxXorSubsequences(self, nums: List[int]) -> int:
        N = max(nums).bit_length()
        f = [0] * N
        for x in nums:
            for bit in range(N - 1, -1, -1):
                if x >> bit & 1:
                    if f[bit] == 0:
                        f[bit] = x
                        break
                    x ^= f[bit]

        res = 0
        for base in f[::-1]:
            if (ans := res ^ base) > res:
                res = ans
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxXorSubsequences(nums)
    print("\noutput:", serialize(ans, "integer"))
