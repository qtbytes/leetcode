# Created by none at 2025/05/02 10:49
# leetgo: 1.4.13
# https://leetcode.com/problems/push-dominoes/

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
    def pushDominoes(self, dominoes: str) -> str:
        res = list(dominoes)
        force = [i for i, v in enumerate(dominoes) if v != "."]
        i = 0
        while i < len(force):
            start = force[i]
            while i + 1 < len(force) and dominoes[force[i + 1]] == dominoes[force[i]]:
                i += 1

            for index in range(start, force[i] + 1):
                res[index] = dominoes[start]

            if i + 1 < len(force) and dominoes[start] == "R":
                end = force[i + 1]
                l, r = force[i], force[i + 1]
                while l < r:
                    res[l] = dominoes[start]
                    res[r] = dominoes[end]
                    l += 1
                    r -= 1
                if l == r:
                    res[l] = "."
            i += 1

        if len(force) > 0:
            if dominoes[force[0]] == "L":
                for i in range(force[0]):
                    res[i] = "L"

            if dominoes[force[-1]] == "R":
                for i in range(force[-1], len(res)):
                    res[i] = "R"

        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    dominoes: str = deserialize("str", read_line())
    ans = Solution().pushDominoes(dominoes)
    print("\noutput:", serialize(ans, "string"))
