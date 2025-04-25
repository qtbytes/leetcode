# Created by none at 2025/04/25 11:44
# leetgo: 1.4.13
# https://leetcode.com/problems/count-of-interesting-subarrays/

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
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0
        for x in nums:
            s += (x % modulo) == k
            s %= modulo
            res += cnt[(s - k) % modulo]
            cnt[s] += 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    modulo: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countInterestingSubarrays(nums, modulo, k)
    print("\noutput:", serialize(ans, "long"))
