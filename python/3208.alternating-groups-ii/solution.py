# Created by none at 2025/03/09 13:55
# leetgo: 1.4.13
# https://leetcode.com/problems/alternating-groups-ii/

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
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        s = 1

        for i in range(1, n - 1 + k):
            if colors[i % n] != colors[(i - 1) % n]:
                s += 1
                if s >= k:
                    res += 1
            else:
                s = 1

        return res


# @lc code=end

if __name__ == "__main__":
    colors: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfAlternatingGroups(colors, k)
    print("\noutput:", serialize(ans, "integer"))
