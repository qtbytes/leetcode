# Created by none at 2024/09/24 14:23
# leetgo: 1.4.9
# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/

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
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        x, y = pattern
        cnt = [0] * 2
        res = 0
        for ch in text:
            if ch == y:
                res += cnt[0]
                cnt[1] += 1
            if ch == x:
                cnt[0] += 1
        return res + max(cnt)


# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    pattern: str = deserialize("str", read_line())
    ans = Solution().maximumSubsequenceCount(text, pattern)
    print("\noutput:", serialize(ans, "long"))
