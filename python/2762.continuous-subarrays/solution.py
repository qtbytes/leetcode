# Created by none at 2024/12/14 15:24
# leetgo: 1.4.9
# https://leetcode.com/problems/continuous-subarrays/

import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import string
from typing import *

from leetgo_py import *

# @lc code=begin


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0
        mx = []
        mn = []
        l = 0
        for r, x in enumerate(nums):
            heapq.heappush(mx, (-x, r))
            heapq.heappush(mn, (x, r))
            while -(mx[0][0]) - mn[0][0] > 2:
                l += 1
                while mx[0][1] < l:
                    heapq.heappop(mx)
                while mn[0][1] < l:
                    heapq.heappop(mn)
            res += r - l + 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().continuousSubarrays(nums)
    print("\noutput:", serialize(ans, "long"))
