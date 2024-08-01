# Created by none at 2024/08/01 13:58
# leetgo: 1.4.7
# https://leetcode.cn/problems/uOAnQW/

from typing import *
from leetgo_py import *

import bisect
import collections
import functools
import heapq
import itertools
import operator
import math
import string

# @lc code=begin


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        q = [[] for _ in range(2)]
        for x in cards:
            q[x & 1].append(x)

        p = [list(itertools.accumulate(sorted(e, reverse=True), initial=0)) for e in q]

        res = 0

        # maybe use 0 2 4 ... odd
        for i in range(0, len(q[1]) + 1, 2):
            j = cnt - i
            if 0 <= j <= len(q[0]):
                # res = max(res, sum(q[1][:i]) + sum(q[0][:j]))
                res = max(res, p[1][i] + p[0][j])
        return res


# @lc code=end

if __name__ == "__main__":
    cards: List[int] = deserialize("List[int]", read_line())
    cnt: int = deserialize("int", read_line())
    ans = Solution().maxmiumScore(cards, cnt)
    print("\noutput:", serialize(ans, "integer"))
