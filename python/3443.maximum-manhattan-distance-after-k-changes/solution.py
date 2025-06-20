# Created by none at 2025/06/20 10:04
# leetgo: dev
# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

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
    def maxDistance(self, s: str, K: int) -> int:
        map = {v: i for i, v in enumerate("NESW")}
        cnt = [0] * 4
        res = 0
        for ch in s:
            cnt[map[ch]] += 1
            ans = 0
            k = K
            for i in range(2):
                x = cnt[i]
                y = cnt[i + 2]
                if x > y:
                    x, y = y, x
                if k >= x:
                    ans += y + x
                    k -= x
                else:
                    ans += y + k - (x - k)
                    k = 0
            res = max(res, ans)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxDistance(s, k)
    print("\noutput:", serialize(ans, "integer"))
