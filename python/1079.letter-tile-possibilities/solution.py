# Created by none at 2025/02/17 15:41
# leetgo: 1.4.13
# https://leetcode.com/problems/letter-tile-possibilities/

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
    def numTilePossibilities(self, tiles: str) -> int:
        s = sorted(tiles)
        n = len(s)
        res = 0
        used = [False] * n

        def dfs(i: int):
            nonlocal res
            res += 1
            if i == n:
                return
            cur_level = set()
            for j, x in enumerate(s):
                if not used[j]:
                    if x not in cur_level:
                        cur_level.add(x)
                        used[j] = True
                        dfs(i + 1)
                        used[j] = False

        dfs(0)
        return res - 1


# @lc code=end

if __name__ == "__main__":
    tiles: str = deserialize("str", read_line())
    ans = Solution().numTilePossibilities(tiles)
    print("\noutput:", serialize(ans, "integer"))
