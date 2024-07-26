# Created by none at 2024/07/27 00:42
# leetgo: 1.4.7
# https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/

from typing import *
from leetgo_py import *

import bisect
import collections
import functools
import heapq
import itertools
import math
from operator import xor
from string import ascii_lowercase

# @lc code=begin


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        t = list(s)
        n = len(s)
        i = 0
        while k > 0 and i < n:
            d = min(ord(s[i]) - ord("a"), ord("a") + 26 - ord(s[i]))
            if d <= k:
                t[i] = "a"
                k -= d
                i += 1
            else:
                t[i] = chr(ord(s[i]) - k)
                break
        return "".join(t)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getSmallestString(s, k)
    print("\noutput:", serialize(ans, "string"))
