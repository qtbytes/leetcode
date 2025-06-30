# Created by none at 2025/06/30 23:26
# leetgo: dev
# https://leetcode.com/problems/longest-harmonious-subsequence/

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
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        r = 0
        n = len(nums)
        for l, x in enumerate(nums):
            while r < n and nums[r] - x <= 1:
                r += 1
            if nums[r - 1] - x == 1:
                res = max(res, r - l)
        return res

        # cnt = Counter(nums)
        # res = 0
        # for x, y in pairwise(sorted(cnt)):
        #     if y - x == 1:
        #         res = max(res, cnt[x] + cnt[y])
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLHS(nums)
    print("\noutput:", serialize(ans, "integer"))
