# Created by none at 2025/05/16 21:56
# leetgo: 1.4.13
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

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
def hamming_distance(s: str, t: str) -> int:
    if len(s) != len(t):
        return -1
    return sum(x != y for x, y in zip(s, t))


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(words)
        f = [1] * n
        before = [-1] * n
        for i, w in enumerate(words):
            for j in range(i + 1, n):
                if groups[j] != groups[i] and hamming_distance(w, words[j]) == 1:
                    if f[i] + 1 > f[j]:
                        f[j] = f[i] + 1
                        before[j] = i
        j = f.index(max(f))
        res = []
        while j >= 0:
            res.append(words[j])
            j = before[j]
        res.reverse()
        return res


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    groups: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getWordsInLongestSubsequence(words, groups)
    print("\noutput:", serialize(ans, "string[]"))
