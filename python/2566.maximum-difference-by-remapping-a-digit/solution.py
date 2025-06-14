# Created by none at 2025/06/14 10:53
# leetgo: dev
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

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
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        i = next((i for i, x in enumerate(s) if x != "9"), -1)
        return int(s.replace(s[i], "9")) - int(s.replace(s[0], "0"))


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().minMaxDifference(num)
    print("\noutput:", serialize(ans, "integer"))
