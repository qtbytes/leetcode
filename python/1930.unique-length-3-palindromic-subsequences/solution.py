# Created by none at 2025/01/04 15:06
# leetgo: 1.4.13
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

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
    def countPalindromicSubsequence(self, s: str) -> int:
        # can be replaced by (first_index, end_index)
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            mp[ch].append(i)

        res = 0
        # enumerate mid char
        for mid, v1 in mp.items():
            # enumerate left char
            for left, v2 in mp.items():
                if len(v2) < 2:
                    continue
                l, r = v2[0], v2[-1]
                # here r + 1 is to handle v1 == v2
                i = bisect_left(v1, l + 1)
                if i < len(v1) and v1[i] < r:
                    res += 1
        return res

        # right = Counter(s)
        # left = Counter()
        # res = 0
        # seen = set()
        # for ch in s:
        #     right[ch] -= 1
        #     for k in left:
        #         if right[k] > 0 and (ch, k) not in seen:
        #             seen.add((ch, k))
        #             res += 1
        #     left[ch] += 1
        # return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countPalindromicSubsequence(s)
    print("\noutput:", serialize(ans, "integer"))
