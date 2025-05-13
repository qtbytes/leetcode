# Created by none at 2025/05/13 10:36
# leetgo: 1.4.13
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

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
N = 26


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = deque([0] * N)
        for ch in s:
            q[ord(ch) - ord("a")] += 1
        for _ in range(t):
            z = q.pop()
            q[0] += z
            q.appendleft(z)
        return sum(q) % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: int = deserialize("int", read_line())
    ans = Solution().lengthAfterTransformations(s, t)
    print("\noutput:", serialize(ans, "integer"))
