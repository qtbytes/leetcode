# Created by none at 2025/04/21 13:32
# leetgo: 1.4.13
# https://leetcode.com/problems/count-the-hidden-sequences/

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
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # find the max and min start
        mx = upper
        mn = lower

        for d in differences:
            # lower <= mn + d <= upper:
            if mn + d > upper:
                return 0
            mn = max(mn, lower - d)
            mn += d
            # lower <= mx + d <= upper:
            if mx + d < lower:
                return 0
            mx = min(mx, upper - d)
            mx += d
        return max(mx - mn + 1, 0)


# @lc code=end

if __name__ == "__main__":
    differences: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().numberOfArrays(differences, lower, upper)
    print("\noutput:", serialize(ans, "integer"))
