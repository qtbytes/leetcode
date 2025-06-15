# Created by none at 2025/06/15 13:02
# leetgo: dev
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

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
    def maxDiff(self, num: int) -> int:
        s = str(num)
        i = next((i for i, x in enumerate(s) if x > "1"), -1)
        mn = num
        if i != -1:
            mn = int(s.replace(s[i], "1")) if i == 0 else int(s.replace(s[i], "0"))

        i = next((i for i, x in enumerate(s) if x != "9"), -1)
        mx = int(s.replace(s[i], "9")) if i != -1 else num
        return mx - mn


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maxDiff(num)
    print("\noutput:", serialize(ans, "integer"))
