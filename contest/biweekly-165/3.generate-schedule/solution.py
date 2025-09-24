# Created by none at 2025/09/23 22:36
# leetgo: dev
# https://leetcode.com/problems/generate-schedule/
# https://leetcode.com/contest/biweekly-contest-165/problems/generate-schedule/

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
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4:
            return []
        res = []
        for step in range(1, n):
            # find start
            x = 0
            if res:
                for i in range(n):
                    if i not in res[-1] and (i + step) % n not in res[-1]:
                        x = i
                        break

            used = set()
            for _ in range(n):
                y = (x + step) % n
                res.append([x, y])
                used.add(x)
                for z in range(1, n):
                    if (x + z) % n in used or set((x, y)) & set(
                        ((x + z) % n, (y + z) % n)
                    ):
                        continue
                    x = (x + z) % n
                    used.add(x)
                    break
                x %= n
        # print(res)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateSchedule(n)
    print("\noutput:", serialize(ans, "integer[][]"))
