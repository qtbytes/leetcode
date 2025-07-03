# Created by none at 2025/07/03 15:20
# leetgo: dev
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

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
    def kthCharacter(self, k: int) -> str:
        def f(x: int) -> int:
            if x == 0:
                return 0
            i = 1
            while i * 2 < x:
                i *= 2
            return (1 + f(x % i)) % 26

        k -= 1  # we want 0 index
        return chr(f(k) + ord("a"))


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().kthCharacter(k)
    print("\noutput:", serialize(ans, "character"))
