# Created by none at 2025/05/06 15:56
# leetgo: 1.4.13
# https://leetcode.com/problems/meeting-rooms-ii/

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
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = defaultdict(int)
        for x, y in intervals:
            diff[x] += 1
            diff[y] -= 1
        res = d = 0
        for x in sorted(diff):
            d += diff[x]
            if d > res:
                res = d
        return res


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minMeetingRooms(intervals)
    print("\noutput:", serialize(ans, "integer"))
