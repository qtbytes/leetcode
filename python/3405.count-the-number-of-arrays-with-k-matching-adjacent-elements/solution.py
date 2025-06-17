# Created by none at 2025/06/17 11:49
# leetgo: dev
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

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
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return m * pow(m - 1, n - k - 1, mod) % mod * (comb(n - 1, k) % mod) % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countGoodArrays(n, m, k)
    print("\noutput:", serialize(ans, "integer"))
