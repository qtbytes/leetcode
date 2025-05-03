# Created by none at 2025/05/03 12:36
# leetgo: 1.4.13
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

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
N = 7


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cnt = [0] * N
        cnt_tops = [0] * N
        cnt_bots = [0] * N
        for x, y in zip(tops, bottoms):
            cnt[x] += 1
            cnt_tops[x] += 1
            cnt_bots[y] += 1
            if x != y:
                cnt[y] += 1

        n = len(tops)
        candidate = [i for i, x in enumerate(cnt) if x == n]
        if not candidate:
            return -1

        res = len(tops)
        for x in candidate:
            res = min(res, n - max(cnt_tops[x], cnt_bots[x]))
        return res


# @lc code=end

if __name__ == "__main__":
    tops: List[int] = deserialize("List[int]", read_line())
    bottoms: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDominoRotations(tops, bottoms)
    print("\noutput:", serialize(ans, "integer"))
