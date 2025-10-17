# Created by none at 2025/10/17 10:54
# leetgo: dev
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        s = [ord(ch) - ord("a") for ch in s]
        n = len(s)
        if k == 26:
            return 1

        @cache
        def dfs(i: int, changed: bool, mask: int):
            if i == n:
                return 1
            new_mask = mask | (1 << s[i])
            if new_mask.bit_count() > k:
                res = 1 + dfs(i + 1, changed, 1 << s[i])
            else:
                res = dfs(i + 1, changed, new_mask)
            if changed:
                return res
            for x in range(26):
                new_mask = mask | (1 << x)
                if new_mask.bit_count() > k:
                    res = max(res, 1 + dfs(i + 1, True, 1 << x))
                else:
                    res = max(res, dfs(i + 1, True, new_mask))
            return res

        return dfs(0, False, 0)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPartitionsAfterOperations(s, k)
    print("\noutput:", serialize(ans, "integer"))
