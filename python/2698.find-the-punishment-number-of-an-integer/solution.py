# Created by none at 2025/02/15 14:27
# leetgo: 1.4.13
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

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
def check(x: int):
    s = str(x * x)
    n = len(s)

    def dfs(i: int, x: int):
        if i == n:
            return x == 0
        num = 0
        for j in range(i + 1, n + 1):
            num = num * 10 + int(s[j - 1])
            if num <= x and dfs(j, x - num):
                return True
        return False

    return dfs(0, x)


N = 1000
f = [0]
s = 0
for x in range(1, N + 1):
    if check(x):
        s += x * x
    f.append(s)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        return f[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().punishmentNumber(n)
    print("\noutput:", serialize(ans, "integer"))
