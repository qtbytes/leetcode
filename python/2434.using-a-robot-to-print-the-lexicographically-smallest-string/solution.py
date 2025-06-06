# Created by none at 2025/06/06 12:19
# leetgo: dev
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

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
    def robotWithString(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        chars = sorted(last, reverse=True)
        res = []
        st = []
        i, r = 0, -1
        while chars:
            ch = chars.pop()
            while st and st[-1] <= ch:
                res.append(st.pop())
            r = max(r, last[ch])
            while i <= r:
                if s[i] == ch:
                    res.append(s[i])
                else:
                    st.append(s[i])
                i += 1
        return "".join(res + st[::-1])


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().robotWithString(s)
    print("\noutput:", serialize(ans, "string"))
