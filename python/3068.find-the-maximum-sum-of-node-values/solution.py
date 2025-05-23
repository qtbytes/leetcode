# Created by none at 2025/05/23 12:28
# leetgo: dev
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

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
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diff = sorted((x ^ k) - x for x in nums)
        res = sum(nums)
        while diff:
            d1 = diff.pop()
            if d1 <= 0 or not diff:
                break
            d2 = diff.pop()
            if d2 >= 0 or abs(d2) < d1:
                res += d1 + d2
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumValueSum(nums, k, edges)
    print("\noutput:", serialize(ans, "long"))
