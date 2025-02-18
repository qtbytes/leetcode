# Created by none at 2025/02/18 14:16
# leetgo: 1.4.13
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

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
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [0] * (n + 1)

        def dfs(i: int):
            if i == len(res):
                return True
            for num in range(1, 10):
                if num in res:
                    continue
                if i == 0 or ((num < res[i - 1]) == (pattern[i - 1] == "D")):
                    res[i] = num
                    if dfs(i + 1):
                        return True
                    res[i] = 0
            return False

        dfs(0)
        return "".join(map(str, res))


# @lc code=end

if __name__ == "__main__":
    pattern: str = deserialize("str", read_line())
    ans = Solution().smallestNumber(pattern)
    print("\noutput:", serialize(ans, "string"))
