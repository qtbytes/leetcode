# Created by none at 2025/12/06 12:43
# leetgo: dev
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

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
from sortedcontainers import SortedList


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        ans = 0
        prefix_sum = [0, 1]
        s = 1
        l = 0

        sl = SortedList()

        for r, x in enumerate(nums):
            while l < r and (abs(x - sl[0]) > k or abs(x - sl[-1]) > k):
                sl.remove(nums[l])
                l += 1
            # ans[r + 1] = sum(ans[l : r + 1]) % mod
            ans = (prefix_sum[r + 1] - prefix_sum[l]) % mod
            s = (s + ans) % mod
            prefix_sum.append(s)
            sl.add(x)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countPartitions(nums, k)
    print("\noutput:", serialize(ans, "integer"))
