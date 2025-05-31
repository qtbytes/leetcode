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
from sortedcontainers import SortedList


class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        def diff(a: deque[int], b: SortedList[int]):
            l = r = -1
            for i, (x, y) in enumerate(zip(a, b)):
                if x != y:
                    if l == -1:
                        l = i
                    r = i
            return (r - l + 1) if l != -1 else 0

        q, sl = deque(), SortedList()
        for i in range(k - 1):
            q.append(nums[i])
            sl.add(nums[i])

        res = []
        for i in range(k - 1, len(nums)):
            q.append(nums[i])
            sl.add(nums[i])

            res.append(diff(q, sl))
            sl.remove(q.popleft())
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minSubarraySort(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
