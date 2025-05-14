# Created by none at 2025/05/14 12:05
# leetgo: 1.4.13
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

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
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        f[0][0]: a transform pow(2, 0) times
        f[0][1]: a transform pow(2, 1) times
        f[0][2]: a transform pow(2, 2) times

        @cache
        dfs(x:int, t:int):
            cnt = dfs(x, t-1)
            res = [0] * 26
            for y, c in enumerate(cnt)
                tmp = dfs(y, t-1)
                res |= tmp
            return res
        """
        N = 26
        mod = 10**9 + 7

        def add(a: list[int], b: list[int], c: int):
            for i in range(N):
                a[i] += b[i] * c
                a[i] %= mod
            return a

        @cache
        def dfs(x: int, t: int):
            # x transform pow(2, t) times
            res = [0] * N
            if t == 0:
                for next in range(x + 1, x + nums[x] + 1):
                    res[next % N] += 1
                return res
            cnt = dfs(x, t - 1)
            for y, c in enumerate(cnt):
                if c == 0:
                    continue
                res = add(res, dfs(y, t - 1), c)
            return res

        cnt = [0] * N
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        while t > 0:
            high_bit = t.bit_length() - 1
            t ^= 1 << high_bit

            res = [0] * N
            for x, c in enumerate(cnt):
                if c == 0:
                    continue
                res = add(res, dfs(x, high_bit), c)

            cnt = res

        return sum(res) % mod


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: int = deserialize("int", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthAfterTransformations(s, t, nums)
    print("\noutput:", serialize(ans, "integer"))
