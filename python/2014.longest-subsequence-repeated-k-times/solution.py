# Created by none at 2025/06/27 14:30
# leetgo: dev
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, permutations, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # `2 <= n < k * 8`  => at most 7 chars has freq >= k
        candidate = []
        for c, v in Counter(s).items():
            candidate.extend([c] * (v // k))
        if not candidate:
            return ""

        def is_sub(t: str, s: iter) -> bool:
            # s is iter, `in` can digest iter
            return all(ch in s for ch in t)

        candidate.sort(reverse=True)  # make sure bigger char first
        for size in range(len(candidate), -1, -1):
            for t in permutations(candidate, size):
                if is_sub(("".join(t)) * k, iter(s)):
                    return "".join(t)

        return ""


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestSubsequenceRepeatedK(s, k)
    print("\noutput:", serialize(ans, "string"))
