# Created by none at 2025/03/15 13:57
# leetgo: 1.4.13
# https://leetcode.com/problems/house-robber-iv/

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
    def minCapability(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = max(nums)

        def check(mid: int) -> bool:
            cnt = 0
            j = -2
            for i, x in enumerate(nums):
                if x <= mid and i - j > 1:
                    cnt += 1
                    j = i
            return cnt >= k

        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCapability(nums, k)
    print("\noutput:", serialize(ans, "integer"))
