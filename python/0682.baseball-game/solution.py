# Created by none at 2024/07/29 11:30
# leetgo: 1.4.7
# https://leetcode.cn/problems/baseball-game/

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
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "D":
                st.append(st[-1] * 2)
            elif op == "C":
                st.pop()
            elif op == "+":
                st.append(st[-1] + st[-2])
            else:
                st.append(int(op))

        return sum(st)


# @lc code=end

if __name__ == "__main__":
    operations: List[str] = deserialize("List[str]", read_line())
    ans = Solution().calPoints(operations)
    print("\noutput:", serialize(ans, "integer"))
