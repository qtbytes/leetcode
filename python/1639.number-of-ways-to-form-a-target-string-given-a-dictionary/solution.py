# Created by none at 2024/12/29 15:07
# leetgo: 1.4.11
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

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
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        m, n = len(words[0]), len(target)
        if m < n:
            return 0

        cnt = [[0] * 26 for _ in range(m)]
        for w in words:
            for j, ch in enumerate(w):
                cnt[j][ord(ch) - ord("a")] += 1

        @cache
        def dfs(i: int, j: int):
            """
            - i means the index selected in word
            - j means the index of target
            """
            if j == n:
                return 1
            if m - i < n - j:
                return 0
            # select word[i]
            res = cnt[i][ord(target[j]) - ord("a")] * dfs(i + 1, j + 1)
            # don't select
            res += dfs(i + 1, j)
            return res % mod

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().numWays(words, target)
    print("\noutput:", serialize(ans, "integer"))
