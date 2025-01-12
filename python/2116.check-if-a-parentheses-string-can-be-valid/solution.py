# Created by none at 2025/01/12 13:27
# leetgo: 1.4.13
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

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
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False
        mx = 0  # maxiumal score
        mn = 0  # minimal score and valid score
        for i, (ch, lock) in enumerate(zip(s, locked)):
            if lock == "1":
                diff = 1 if ch == "(" else -1
                mx += diff
                mn = max(mn + diff, (i + 1) & 1)
            else:
                mx += 1
                mn = max(mn - 1, (i + 1) & 1)
            if mx < mn:
                return False
        return mn == 0


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    locked: str = deserialize("str", read_line())
    ans = Solution().canBeValid(s, locked)
    print("\noutput:", serialize(ans, "boolean"))
