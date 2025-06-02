# Created by none at 2025/05/31 20:00
# leetgo: dev
# https://leetcode.com/problems/minimum-time-to-visit-all-houses/

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
    def minTotalTime(
        self, forward: List[int], backward: List[int], queries: List[int]
    ) -> int:
        forward_prefix = list(accumulate(forward, initial=0))
        backward_prefix = list(accumulate(backward[::-1], initial=0))[::-1]
        x = 0
        res = 0
        for y in queries:
            if x <= y:
                forward_cost = forward_prefix[y] - forward_prefix[x]
                backward_cost = (
                    backward_prefix[0] - backward_prefix[x + 1] + backward_prefix[y + 1]
                )
            else:
                forward_cost = (
                    forward_prefix[-1] - forward_prefix[x] + forward_prefix[y]
                )
                backward_cost = backward_prefix[y + 1] - backward_prefix[x + 1]

            res += min(forward_cost, backward_cost)
            x = y
        return res


# @lc code=end

if __name__ == "__main__":
    forward: List[int] = deserialize("List[int]", read_line())
    backward: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minTotalTime(forward, backward, queries)
    print("\noutput:", serialize(ans, "long"))
