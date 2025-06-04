# Created by none at 2025/06/04 14:03
# leetgo: dev
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

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
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        m = n - numFriends + 1
        return max(word[i : i + m] for i in range(n))


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    numFriends: int = deserialize("int", read_line())
    ans = Solution().answerString(word, numFriends)
    print("\noutput:", serialize(ans, "string"))
