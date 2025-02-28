# Created by none at 2025/02/28 14:05
# leetgo: 1.4.13
# https://leetcode.com/problems/shortest-common-supersequence/

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
def lcs(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    f = [[0] * (n + 1) for _ in range(m + 1)]
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                f[i + 1][j + 1] = 1 + f[i][j]
            else:
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
    res = []
    i, j = m, n
    while i > 0 and j > 0:
        if f[i][j] == f[i - 1][j]:
            i -= 1
        elif f[i][j] == f[i][j - 1]:
            j -= 1
        else:
            res.append(s1[i - 1])
            i -= 1
            j -= 1
    return "".join(res[::-1])


class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        s = lcs(s1, s2)
        i = j = 0
        m, n = len(s1), len(s2)
        res = []
        for ch in s:
            i1 = i
            while i1 < m and s1[i1] != ch:
                i1 += 1
            res.extend((s1[i:i1]))
            j1 = j
            while j1 < n and s2[j1] != ch:
                j1 += 1
            res.extend((s2[j:j1]))
            res.append(ch)
            i = i1 + 1
            j = j1 + 1
        res.extend(s1[i:])
        res.extend(s2[j:])

        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    str1: str = deserialize("str", read_line())
    str2: str = deserialize("str", read_line())
    ans = Solution().shortestCommonSupersequence(str1, str2)
    print("\noutput:", serialize(ans, "string"))
