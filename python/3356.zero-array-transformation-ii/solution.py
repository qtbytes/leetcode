# Created by none at 2025/03/13 15:05
# leetgo: 1.4.13
# https://leetcode.com/problems/zero-array-transformation-ii/

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
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(mid: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for k in range(mid):
                i, j, v = queries[k]
                diff[i] += v
                diff[j + 1] -= v
            # print(mid, nums, diff)
            s = 0  # prefix sum
            for i, x in enumerate(nums):
                s += diff[i]
                # print(s, x)
                if s < x:
                    return False
            return True

        n = len(queries)
        res = bisect_left(range(0, len(queries) + 1), True, key=check)
        if res > n:
            return -1
        return res
        # n = len(queries)
        # l = 0
        # r = n + 1

        # while l < r:
        #     mid = (l + r) >> 1
        #     if check(mid):
        #         r = mid
        #     else:
        #         l = mid + 1
        # if l > n:
        #     return -1
        # return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minZeroArray(nums, queries)
    print("\noutput:", serialize(ans, "integer"))
