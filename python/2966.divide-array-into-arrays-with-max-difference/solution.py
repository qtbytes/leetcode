# Created by none at 2025/06/18 13:16
# leetgo: dev
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

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
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i : i + 3])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().divideArray(nums, k)
    print("\noutput:", serialize(ans, "integer[][]"))
