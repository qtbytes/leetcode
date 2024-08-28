# Created by none at 2024/08/28 13:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/

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
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        @functools.cache
        def dfs(i: int):
            if i == n:
                return 0
            cnt = collections.Counter()
            mx = 0
            res = math.inf
            for j in range(i, n):
                ch = s[j]
                cnt[ch] += 1
                mx = max(cnt[ch], mx)
                if mx * len(cnt) == j - i + 1:
                    res = min(res, 1 + dfs(j + 1))
            return res

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumSubstringsInPartition(s)
    print("\noutput:", serialize(ans, "integer"))
