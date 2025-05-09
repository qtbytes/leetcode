# Created by none at 2025/05/09 15:40
# leetgo: 1.4.13
# https://leetcode.com/problems/count-number-of-balanced-permutations/

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

N = 10


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7

        cnt, s = [0] * N, 0
        for x in map(int, num):
            cnt[x] += 1
            s += x

        if s & 1:
            return 0

        n = len(num)
        half = n // 2

        @cache
        def dfs(x: int, i: int, target: int):
            if x == -1:
                return int(i == 0 and target == 0)
            j = (n - half) - (sum(cnt[x + 1 :]) - (half - i))
            if i < 0 or j < 0:
                return 0

            res = 0
            for k in range(min(cnt[x], i) + 1):
                res += (
                    comb(i, k)
                    * comb(j, cnt[x] - k)
                    * dfs(x - 1, i - k, target - x * k)
                    % mod
                )
            return res % mod

        return dfs(N - 1, half, s // 2)


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().countBalancedPermutations(num)
    print("\noutput:", serialize(ans, "integer"))
