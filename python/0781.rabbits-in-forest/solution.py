# Created by none at 2025/04/20 12:06
# leetgo: 1.4.13
# https://leetcode.com/problems/rabbits-in-forest/

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
    def numRabbits(self, answers: List[int]) -> int:
        return len(answers) + sum(
            k + 1 - v % (k + 1) for k, v in Counter(answers).items() if v % (k + 1) != 0
        )


# @lc code=end

if __name__ == "__main__":
    answers: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numRabbits(answers)
    print("\noutput:", serialize(ans, "integer"))
