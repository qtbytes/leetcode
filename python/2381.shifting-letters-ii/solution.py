# Created by none at 2025/01/05 20:29
# leetgo: 1.4.13
# https://leetcode.com/problems/shifting-letters-ii/

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
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            dx = -1
            if direction == 1:
                dx = 1
            diff[start] += dx
            diff[end + 1] -= dx

        d = 0
        res = []
        for i, ch in enumerate(s):
            d += diff[i]
            res.append(chr((ord(ch) - ord("a") + d) % 26 + ord("a")))

        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    shifts: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shiftingLetters(s, shifts)
    print("\noutput:", serialize(ans, "string"))
