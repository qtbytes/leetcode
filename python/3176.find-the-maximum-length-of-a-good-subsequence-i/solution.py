# Created by none at 2024/09/06 14:27
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/

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
    def maximumLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return max(collections.Counter(nums).values())

        @functools.cache
        def dfs(i: int, k: int, last: int):
            if i == -1:
                return 0
            # choose nums[i]
            res = 0
            if (_k := k - int(not (last == 0 or nums[i] == last))) >= 0:
                res = 1 + dfs(i - 1, _k, nums[i])
            # don't choose
            res = max(res, dfs(i - 1, k, last))
            return res

        res = dfs(len(nums) - 1, k, 0)
        dfs.cache_clear()
        return res

        # @functools.cache
        # def dfs(i: int, k: int):
        #     if i == -1:
        #         return 0
        #     res = dfs(i - 1, k)
        #     for j in range(i - 1, -1, -1):
        #         if (_k := k - int(nums[i] != nums[j])) >= 0:
        #             # print(i, j, k, _k)
        #             res = max(res, 1 + dfs(j, _k))
        #     # print(i, k, res)
        #     return res
        #
        # res = dfs(len(nums) - 1, k)
        # dfs.cache_clear()
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))
