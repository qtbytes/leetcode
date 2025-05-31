# Created by none at 2025/05/31 19:42
# leetgo: dev
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        def diff(a: list[int], b: list[int]):
            l = r = -1
            for i, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    if l == -1:
                        l = i
                    r = i
            return (r - l + 1) if l != -1 else 0

        return [
            diff(nums[i - k : i], sorted(nums[i - k : i]))
            for i in range(k, len(nums) + 1)
        ]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minSubarraySort(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
