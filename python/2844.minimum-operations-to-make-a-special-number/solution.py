# Created by none at 2024/07/25 08:50
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/

from typing import *
from leetgo_py import *

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

# @lc code=begin


class Solution:
    def minimumOperations(self, num: str) -> int:
        res = n = len(num)
        mp = defaultdict(list)
        for i, x in enumerate(map(int, num)):
            if x in (0, 2, 5, 7):
                mp[x].append(i)

        def f(v: list[int], x: int):
            nonlocal res
            i = bisect_left(v, x)
            if i > 0:
                res = min(res, n - v[i - 1] - 2)

        if mp[0]:
            # 00 or 50
            res = n - 1  # "0"
            if len(mp[0]) >= 2:
                res = min(res, n - mp[0][-2] - 2)
            f(mp[5], mp[0][-1])

        if mp[5]:
            # 25 or 75
            f(mp[2], mp[5][-1])
            f(mp[7], mp[5][-1])
        return res


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().minimumOperations(num)
    print("\noutput:", serialize(ans, "integer"))
