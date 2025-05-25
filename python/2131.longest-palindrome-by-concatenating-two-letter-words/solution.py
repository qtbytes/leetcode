# Created by none at 2025/05/25 11:41
# leetgo: dev
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        res = 0
        for w in words:
            rev = w[::-1]
            if seen[rev] > 0:
                res += 2
                seen[rev] -= 1
            else:
                seen[w] += 1

        return (res + max((c for w, c in seen.items() if w[0] == w[1]), default=0)) * 2


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestPalindrome(words)
    print("\noutput:", serialize(ans, "integer"))
