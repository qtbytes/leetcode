# Created by none at 2025/07/01 16:38
# leetgo: dev
# https://leetcode.com/problems/find-the-original-typed-string-i/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, groupby, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        n, i = len(word), 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            res += j - i - 1
            i = j
        return res
        # res = 1  # origin
        # for _, g in groupby(word):
        #     n = len(list(g))
        #     # keep `1..n` char
        #     res += n - 1
        # return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().possibleStringCount(word)
    print("\noutput:", serialize(ans, "integer"))
