# Created by none at 2025/04/28 11:15
# leetgo: 1.4.13
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        sum = 0
        res = 0
        for r, x in enumerate(nums):
            sum += x
            while sum * (r - l + 1) >= k:
                sum -= nums[l]
                l += 1
            res += r - l + 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)
    print("\noutput:", serialize(ans, "long"))
