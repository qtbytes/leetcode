# Created by none at 2025/03/04 13:48
# leetgo: 1.4.13
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

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

i = 1
q = []
while i < 10**7:
    q.append(i)
    i *= 3

N = len(q)  # N is not greater than 16
ok = set()
# O(pow(2, 16) * 16)
for mask in range(1 << N):
    s = 0
    for i in range(N):
        if mask >> i & 1:
            s += pow(3, i)
    ok.add(s)


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return n in ok
        # def dfs(i: int, n: int):
        #     if n == 0:
        #         return True
        #     if i == len(q) or n < 0:
        #         return False
        #     if pow(3, i) > n:
        #         return False
        #     return dfs(i + 1, n - pow(3, i)) or dfs(i + 1, n)

        # return dfs(0, n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().checkPowersOfThree(n)
    print("\noutput:", serialize(ans, "boolean"))
