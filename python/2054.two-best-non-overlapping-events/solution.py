# Created by none at 2025/12/23 13:32
# leetgo: dev
# https://leetcode.com/problems/two-best-non-overlapping-events/

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
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[1])
        # print(events)
        ans = 0
        pre = []
        for start, end, value in events:
            ans = max(ans, value)
            i = bisect_left(pre, (start, 0))
            # print(pre, i)
            if i > 0:
                ans = max(ans, pre[i - 1][1] + value)
            if not pre or value > pre[-1][1]:
                pre.append((end, value))
        return ans


# @lc code=end

if __name__ == "__main__":
    events: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTwoEvents(events)
    print("\noutput:", serialize(ans, "integer"))
