# Created by none at 2024/07/26 11:00
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-value-of-the-partition/

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
# from bisect import bisect_left, bisect_right
# from collections import Counter, defaultdict, deque
# from functools import cache, cmp_to_key, lru_cache, reduce
# from heapq import heapify, heappop, heappush, heappushpop, heapreplace
# from icecream import ic
# from itertools import accumulate, chain, count, pairwise, zip_longest
# from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
# from operator import xor
# from pprint import pprint
# from string import ascii_lowercase
# from typing import List, Optional

# @lc code=begin


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(y - x for x, y in itertools.pairwise(nums))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findValueOfPartition(nums)
    print("\noutput:", serialize(ans, "integer"))
