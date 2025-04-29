# Created by none at 2025/04/29 12:33
# leetgo: 1.4.13
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        res = 0
        a = []
        for i, x in enumerate(nums):
            if x == mx:
                a.append(i)
            if len(a) >= k:
                res += a[-(k)] + 1
        return res

        # Solution of maximum element of subarray

        # n = len(nums)
        # left = [0] * n
        # right = [n - 1] * n
        # mp = defaultdict(list)
        # st = []
        # for i, x in enumerate(nums):
        #     mp[x].append(i)
        #     while st and x >= nums[st[-1]]:
        #         right[st.pop()] = i - 1
        #     if st:
        #         left[i] = st[-1] + 1
        #     st.append(i)

        # res = 0
        # for x, l, r in zip(nums, left, right):
        #     v = mp[x]
        #     i = bisect_right(v, r) - 1
        #     if i >= k - 1 and v[i - (k - 1)] >= l:
        #         res += (v[i - (k - 1)] - l + 1) * (r - v[i] + 1)
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)
    print("\noutput:", serialize(ans, "long"))
