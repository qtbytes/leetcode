# Created by none at 2025/06/17 14:22
# leetgo: dev
# https://leetcode.com/problems/number-of-music-playlists/

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


class Solution:
    def numMusicPlaylists(self, n: int, m: int, k: int) -> int:
        @cache
        def dfs(i: int, unused: int) -> int:
            if i == m:
                return unused == 0
            used = n - unused
            res = 0
            if unused > 0:
                res = unused * dfs(i + 1, unused - 1)
            if i >= k:
                # songs used but not in [i-k..i]
                res += (used - k) % mod * dfs(i + 1, unused) % mod
            return res % mod

        return dfs(0, n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    goal: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numMusicPlaylists(n, goal, k)
    print("\noutput:", serialize(ans, "integer"))
