# Created by none at 2025/05/12 15:42
# leetgo: 1.4.13
# https://leetcode.com/problems/finding-3-digit-even-numbers/

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
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        if all(x & 1 for x in digits) or all(x == 0 for x in digits):
            return res

        cnt = [0] * 10
        for x in digits:
            cnt[x] += 1

        def dfs(i: int, ans: int):
            if i == 3:
                res.append(ans)
                return
            for x, c in enumerate(cnt):
                if c > 0 and not (x & 1 and i == 2 or x == 0 and i == 0):
                    cnt[x] -= 1
                    dfs(i + 1, ans * 10 + x)
                    cnt[x] += 1

        dfs(0, 0)

        return res


# @lc code=end

if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findEvenNumbers(digits)
    print("\noutput:", serialize(ans, "integer[]"))
