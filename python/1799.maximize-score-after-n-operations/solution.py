# Created by none at 2025/06/17 16:01
# leetgo: dev
# https://leetcode.com/problems/maximize-score-after-n-operations/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, combinations, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-inf] * (1 << n)
        dp[0] = 0

        @cache
        def gcd_cache(x, y) -> int:
            return gcd(x, y)

        for mask in range(1 << n):
            bit = [j for j, _ in enumerate(nums) if mask >> j & 1]
            i = len(bit) // 2
            if len(bit) & 1 == 0:
                for x, y in combinations(bit, 2):
                    score = i * gcd_cache(nums[x], nums[y])
                    new_mask = mask ^ (1 << x) ^ (1 << y)
                    dp[mask] = max(dp[mask], dp[new_mask] + score)
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScore(nums)
    print("\noutput:", serialize(ans, "integer"))
