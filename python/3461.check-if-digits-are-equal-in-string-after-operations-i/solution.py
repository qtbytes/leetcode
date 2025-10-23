# Created by none at 2025/10/23 14:15
# leetgo: dev
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

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
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))
        for _ in range(2, len(s)):
            for i in range(len(s) - 1):
                s[i] = (s[i] + s[i + 1]) % 10
            s.pop()
        return s[0] == s[1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().hasSameDigits(s)
    print("\noutput:", serialize(ans, "boolean"))
