# Created by none at 2025/05/26 13:27
# leetgo: dev
# https://leetcode.com/problems/count-the-number-of-good-subsequences/

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
mod = 10**9 + 7

N = 10**4 + 1
fac = [1] * N
for i in range(1, N):
    fac[i] = i * fac[i - 1] % mod


@cache
def my_comb(m: int, n: int):
    return fac[m] * pow(fac[m - n], -1, mod) % mod * pow(fac[n], -1, mod) % mod


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        for n in range(1, max(cnt.values()) + 1):
            cur = 1
            for m in cnt.values():
                if m >= n:
                    cur = cur * (my_comb(m, n) + 1) % mod
            res = (res + cur - 1) % mod
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countGoodSubsequences(s)
    print("\noutput:", serialize(ans, "integer"))
