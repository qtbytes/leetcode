# Created by none at 2025/02/19 18:48
# leetgo: 1.4.13
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

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
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        k -= 1
        if k >= 3 * pow(2, n - 1):
            return ""

        for i in reversed(range(n)):
            can_use = list("abc")
            if res:
                can_use.remove(res[-1])
            j = k // pow(2, i)
            res.append(can_use[j])
            k -= j * pow(2, i)
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getHappyString(n, k)
    print("\noutput:", serialize(ans, "string"))
