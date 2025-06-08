# Created by none at 2025/06/08 10:52
# leetgo: dev
# https://leetcode.com/problems/lexicographical-numbers/

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


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(i: int, x: int):
            if x > n:
                return
            res.append(x)
            for y in range(10):
                dfs(i + 1, x * 10 + y)

        for x in range(1, min(n, 9) + 1):
            dfs(1, x)

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().lexicalOrder(n)
    print("\noutput:", serialize(ans, "integer[]"))
