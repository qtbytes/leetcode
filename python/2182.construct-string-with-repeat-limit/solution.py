# Created by none at 2024/12/17 12:55
# leetgo: 1.4.11
# https://leetcode.com/problems/construct-string-with-repeat-limit/

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
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        q = sorted(cnt.items(), reverse=True)
        n = len(q)
        res = []
        for i in range(n):
            ch, c = q[i]
            while c > repeatLimit:
                res.append(ch * repeatLimit)
                c -= repeatLimit
                ok = False
                for j in range(i + 1, n):
                    if q[j][1] > 0:
                        res.append(q[j][0])
                        q[j] = (q[j][0], q[j][1] - 1)
                        ok = True
                        break
                if not ok:
                    c = 0
                    break
            if c:
                res.append(ch * c)
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    repeatLimit: int = deserialize("int", read_line())
    ans = Solution().repeatLimitedString(s, repeatLimit)
    print("\noutput:", serialize(ans, "string"))
