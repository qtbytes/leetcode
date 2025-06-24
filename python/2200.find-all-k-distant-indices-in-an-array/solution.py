# Created by none at 2025/06/24 21:57
# leetgo: dev
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

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
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        diff = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x == key:
                l = max(i - k, 0)
                diff[l] += 1
                r = min(i + k, n - 1)
                diff[r + 1] -= 1
        res = []
        s = 0
        for i, d in enumerate(diff):
            s += d
            if s > 0:
                res.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    key: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKDistantIndices(nums, key, k)
    print("\noutput:", serialize(ans, "integer[]"))
