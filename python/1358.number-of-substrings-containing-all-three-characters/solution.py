# Created by none at 2025/03/11 14:20
# leetgo: 1.4.13
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

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
    def numberOfSubstrings(self, s: str) -> int:
        seen = [-1] * 3
        res = 0
        for i, ch in enumerate(s):
            seen[ord(ch) - ord("a")] = i
            # s[j:i] is valid for j in [0..=left]
            res += min(seen) + 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfSubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
