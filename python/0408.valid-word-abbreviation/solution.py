# Created by none at 2025/05/06 15:26
# leetgo: 1.4.13
# https://leetcode.com/problems/valid-word-abbreviation/

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
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = 0

        while j < n:
            if abbr[j].isalpha():
                if i >= m or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False
                k = j + 1
                while k < n and abbr[k].isdigit():
                    k += 1
                length = int(abbr[j:k])
                if i + length > m:
                    return False
                j = k
                i += length
        return i == m


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    abbr: str = deserialize("str", read_line())
    ans = Solution().validWordAbbreviation(word, abbr)
    print("\noutput:", serialize(ans, "boolean"))
