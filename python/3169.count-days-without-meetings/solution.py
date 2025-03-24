# Created by none at 2025/03/24 13:16
# leetgo: 1.4.13
# https://leetcode.com/problems/count-days-without-meetings/

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
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = 0
        i, n = 0, len(meetings)
        while i < n:
            l, r = meetings[i]
            if i == 0:
                res += max(0, l - 1)

            j = i + 1
            while j < n and meetings[j][0] <= r:
                r = max(meetings[j][1], r)
                j += 1

            if j < n:
                res += meetings[j][0] - r - 1
            else:
                res += max(0, days - r)

            i = j
        return res

        # Diff Array + HashMap

        # q = set((x for m in meetings for x in [m[0], m[1] + 1]))
        # q.add(1)
        # q.add(days + 1)
        # nums = sorted(q)
        # map = {v: i for i, v in enumerate(nums)}
        # n = len(map)

        # diff = [0] * (n + 1)
        # for x, y in meetings:
        #     diff[map[x]] += 1
        #     diff[map[y + 1]] -= 1

        # res = 0

        # prefix = 0
        # for i in range(n - 1):
        #     prefix += diff[i]
        #     if prefix == 0 and nums[i] <= days:
        #         res += nums[i + 1] - nums[i]

        # return res


# @lc code=end

if __name__ == "__main__":
    days: int = deserialize("int", read_line())
    meetings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countDays(days, meetings)
    print("\noutput:", serialize(ans, "integer"))
