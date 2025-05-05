# Created by none at 2025/05/05 12:57
# leetgo: 1.4.13
# https://leetcode.com/problems/domino-and-tromino-tiling/

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
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7

        @cache
        def dfs(i: int, extra: bool) -> int:
            if i == 0:
                return int(not extra)
            if i < 0:
                return 0
            if not extra:
                res = dfs(i - 1, extra) + 2 * dfs(i - 1, not extra) + dfs(i - 2, extra)
            else:
                res = dfs(i - 1, extra) + dfs(i - 2, not extra)
            # print(i, extra, res)
            return res % mod

        return dfs(n, False)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numTilings(n)
    print("\noutput:", serialize(ans, "integer"))
