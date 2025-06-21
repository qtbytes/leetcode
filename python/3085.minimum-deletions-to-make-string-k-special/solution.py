# Created by none at 2025/06/21 12:36
# leetgo: dev
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

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
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        q = sorted(cnt.values())

        if q[-1] - q[0] <= k:
            return 0

        res = inf
        l = r = 0
        prefix = list(accumulate(q, initial=0))

        # the minimal freq must in q
        for i in q:
            while q[l] < i:
                l += 1
            while r < len(q) and q[r] <= i + k:
                r += 1
            # delete q[:l], (for x in q[r:]) x => i+k
            ans = prefix[l] + prefix[-1] - prefix[r] - (i + k) * (len(q) - r)
            res = min(res, ans)
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumDeletions(word, k)
    print("\noutput:", serialize(ans, "integer"))
