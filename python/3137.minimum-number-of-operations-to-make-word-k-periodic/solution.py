# Created by none at 2024/08/17 09:52
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/

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
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word) // k
        cnt = Counter(word[i : i + k] for i in range(0, len(word), k))
        return n - max(cnt.values())


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumOperationsToMakeKPeriodic(word, k)
    print("\noutput:", serialize(ans, "integer"))
