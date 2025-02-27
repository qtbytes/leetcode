# Created by none at 2025/02/27 13:48
# leetgo: 1.4.13
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

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
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Since fib increase like pow(2, n)
        # so the longest length is <= log(2,1000)
        # we can brute force find the ans
        can = set(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i):
                x, y = arr[j], arr[i]
                cnt = 2
                while x + y in can:
                    cnt += 1
                    x, y = y, x + y
                if cnt != 2:  # not fib
                    res = max(res, cnt)
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lenLongestFibSubseq(arr)
    print("\noutput:", serialize(ans, "integer"))
