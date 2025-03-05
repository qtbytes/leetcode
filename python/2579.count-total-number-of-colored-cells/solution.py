# Created by none at 2025/03/05 13:28
# leetgo: 1.4.13
# https://leetcode.com/problems/count-total-number-of-colored-cells/

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
    def coloredCells(self, n: int) -> int:
        # res = 1
        # for i in range(1, n):
        #     res += 4 * i
        # return res
        # return 1 + sum(4 * i for i in range(1, n))
        return 1 + 2 * n * (n - 1)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().coloredCells(n)
    print("\noutput:", serialize(ans, "long"))
