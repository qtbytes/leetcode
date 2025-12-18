# Created by none at 2025/05/23 17:09
# leetgo: dev
# https://leetcode.com/problems/find-the-celebrity/

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


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int):
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        @cache
        def cached_knows(a: int, b: int) -> bool:
            return knows(a, b)

        candidate = 0
        for other in range(1, n):
            # if yes: a is absolutely not celebrity
            # else: b is absolutely not celebrity
            if cached_knows(candidate, other):
                candidate = other

        def is_celecrity(b: int) -> bool:
            for a in range(n):
                if a == b:
                    continue
                if not (cached_knows(a, b) and not cached_knows(b, a)):
                    return False
            return True

        return candidate if is_celecrity(candidate) else -1


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findCelebrity(graph)
    print("\noutput:", serialize(ans, "integer"))
