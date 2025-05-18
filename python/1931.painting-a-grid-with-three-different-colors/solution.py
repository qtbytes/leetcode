# Created by none at 2025/05/18 13:01
# leetgo: dev
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
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
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        if m == 1:
            return 3 * pow(2, n - 1, mod) % mod

        valid = {}
        for mask in range(pow(3, m)):
            colors = []
            x = mask
            for _ in range(m):
                colors.append(x % 3)
                x //= 3
            if all(x != y for x, y in pairwise(colors)):
                valid[mask] = colors

        next = defaultdict(list)
        for mask1, colors1 in valid.items():
            for mask2, colors2 in valid.items():
                if all(x != y for x, y in zip(colors1, colors2)):
                    next[mask1].append(mask2)

        @cache
        def dfs(i: int, last_mask: int):
            if i == 0:
                return 1
            return sum(dfs(i - 1, cur_mask) for cur_mask in next[last_mask]) % mod

        return sum(dfs(n - 1, x) for x in valid) % mod


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().colorTheGrid(m, n)
    print("\noutput:", serialize(ans, "integer"))
