# Created by none at 2025/06/28 13:24
# leetgo: dev
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

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
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(sorted(nums)[-k:])
        res = []
        for x in nums:
            if cnt[x] > 0:
                res.append(x)
                cnt[x] -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSubsequence(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
