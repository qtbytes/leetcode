# Created by none at 2024/07/30 12:22
# leetgo: 1.4.7
# https://leetcode.cn/problems/double-modular-exponentiation/

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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        """
        - `((aᵢᵇ % 10)ᶜ) % mᵢ == target`
        - `1 <= aᵢ, bᵢ, cᵢ, mᵢ <= 10³`
        - `0 <= target <= 10³`
        """
        res = []

        def check(a, b, c, m):
            if m <= target:
                return False
            # quick pow
            return pow(pow(a % 10, b, 10), c, m) == target

        for i, item in enumerate(variables):
            if check(*item):
                res.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    variables: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().getGoodIndices(variables, target)
    print("\noutput:", serialize(ans, "integer[]"))
