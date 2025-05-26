# Created by none at 2025/05/26 17:14
# leetgo: dev
# https://leetcode.com/problems/number-of-divisible-substrings/

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
    def countDivisibleSubstrings(self, word: str) -> int:
        mp = {ch: (i + 1) // 3 for i, ch in enumerate(ascii_lowercase)}

        res = 0
        for i in range(10):
            cnt = defaultdict(int)
            cnt[0] = 1
            s = 0
            for ch in word:
                s += mp[ch] - i
                res += cnt[s]
                cnt[s] += 1
        return res

        # n = len(word)
        # res = 0
        # for i in range(n):
        #     s = 0
        #     for j in range(i, n):
        #         s += mp[word[j]]
        #         res += s % (j - i + 1) == 0
        # return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().countDivisibleSubstrings(word)
    print("\noutput:", serialize(ans, "integer"))
