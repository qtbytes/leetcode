# Created by none at 2025/09/23 22:36
# leetgo: dev
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/
# https://leetcode.com/contest/biweekly-contest-165/problems/minimum-discards-to-balance-inventory/

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
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        res = 0
        q = deque()
        for i, x in enumerate(arrivals):
            if q and q[0][1] + w <= i:
                cnt[q.popleft()[0]] -= 1
            if cnt[x] + 1 > m:
                res += 1
                continue
            cnt[x] += 1
            q.append((x, i))
            # print(q)

        return res


# @lc code=end

if __name__ == "__main__":
    arrivals: List[int] = deserialize("List[int]", read_line())
    w: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().minArrivalsToDiscard(arrivals, w, m)
    print("\noutput:", serialize(ans, "integer"))
