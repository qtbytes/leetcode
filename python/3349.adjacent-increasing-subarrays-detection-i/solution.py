# Created by none at 2025/10/14 11:28
# leetgo: dev
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

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
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                f[i] = f[i - 1] + 1

        for i in range(n - k):
            if f[i] >= k and f[i + k] >= k:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().hasIncreasingSubarrays(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
