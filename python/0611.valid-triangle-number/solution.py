# Created by none at 2025/09/26 12:39
# leetgo: dev
# https://leetcode.com/problems/valid-triangle-number/

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
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        res = 0
        for i in range(n - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                # k = bisect_left(nums, nums[i] + nums[j])
                target = nums[i] + nums[j]
                while k < n and nums[k] < target:
                    k += 1
                if k == n:
                    # 1..=n-j-1
                    res += (n - j) * (n - j - 1) // 2
                    break
                # can use [j+1:k]
                res += k - j - 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().triangleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
