# Created by none at 2025/03/07 13:55
# leetgo: 1.4.13
# https://leetcode.com/problems/closest-prime-numbers-in-range/

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
N = int(1e6) + 1
f = [True] * N
f[0] = f[1] = False
for i in range(2, N):
    if not f[i]:
        continue
    for j in range(i + i, N, i):
        f[j] = False
p = [i for i, v in enumerate(f) if v]


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        i = bisect_left(p, left)
        j = bisect_right(p, right) - 1
        if i >= j:
            return [-1, -1]
        i1 = i
        for k in range(i + 1, j):
            if p[k + 1] - p[k] < p[i1 + 1] - p[i1]:
                i1 = k
        return [p[i1], p[i1 + 1]]


# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().closestPrimes(left, right)
    print("\noutput:", serialize(ans, "integer[]"))
