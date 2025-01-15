# Created by none at 2025/01/15 11:10
# leetgo: 1.4.13
# https://leetcode.com/problems/minimize-xor/

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
    def minimizeXor(self, x: int, y: int) -> int:
        m, n = x.bit_count(), y.bit_count()
        res = 0
        if m >= n:
            for _ in range(n):
                m = x.bit_length()
                highest = 1 << (m - 1)
                res |= highest
                x ^= highest
        else:
            res |= x
            i = 0
            for _ in range(n - m):
                while x >> i & 1 == 1:
                    i += 1
                res |= 1 << i
                i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    num1: int = deserialize("int", read_line())
    num2: int = deserialize("int", read_line())
    ans = Solution().minimizeXor(num1, num2)
    print("\noutput:", serialize(ans, "integer"))
