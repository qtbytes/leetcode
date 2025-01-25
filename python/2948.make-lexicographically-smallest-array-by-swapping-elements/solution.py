# Created by none at 2025/01/25 17:14
# leetgo: 1.4.13
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import *
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        q = sorted(set(nums))
        n = len(q)
        i = 0
        group = {}
        group_index = 0
        while i < n:
            group[q[i]] = group_index
            j = i + 1
            while j < n and q[j] - q[j - 1] <= limit:
                group[q[j]] = group_index
                j += 1
            group_index += 1
            i = j

        indexs = [[] for _ in range(group_index)]
        values = [[] for _ in range(group_index)]
        for i, x in enumerate(nums):
            indexs[group[x]].append(i)
            values[group[x]].append(x)

        for index, value in zip(indexs, values):
            value.sort()
            for i, v in zip(index, value):
                nums[i] = v
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().lexicographicallySmallestArray(nums, limit)
    print("\noutput:", serialize(ans, "integer[]"))
