# Created by none at 2025/02/25 12:43
# leetgo: 1.4.13
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

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
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        s = 0
        cnt = [1, 0]
        for x in arr:
            s ^= x & 1
            res += cnt[s ^ 1]
            cnt[s] += 1
        return res % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numOfSubarrays(arr)
    print("\noutput:", serialize(ans, "integer"))
