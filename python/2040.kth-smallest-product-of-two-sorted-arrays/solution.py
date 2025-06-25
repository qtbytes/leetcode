# Created by none at 2025/06/25 13:52
# leetgo: dev
# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def split(nums: list[int]):
            i = bisect_left(nums, 0)
            return nums[:i], nums[i:]

        neg_x, pos_x = split(nums1)
        neg_y, pos_y = split(nums2)

        neg_count = len(neg_x) * len(pos_y) + len(neg_y) * len(pos_x)

        def check(mid: int, a: list[int], b: list[int]):
            if not a or not b:
                return 0
            j = len(b) - 1
            res = 0
            for x in a:
                while j >= 0 and x * b[j] > mid:
                    j -= 1
                res += j + 1
            return res

        # handle negative product
        if k <= neg_count:
            pos_x.reverse()
            pos_y.reverse()
            l = int(-1e10)
            r = 0

            while l < r:
                mid = (l + r) >> 1
                if check(mid, neg_x, pos_y) + check(mid, pos_x, neg_y) < k:
                    l = mid + 1
                else:
                    r = mid
            return r
        else:
            k -= neg_count
            neg_x.reverse()
            neg_y.reverse()
            l = 0
            r = int(1e10) + 1

            while l < r:
                mid = (l + r) >> 1
                if check(mid, neg_x, neg_y) + check(mid, pos_x, pos_y) < k:
                    l = mid + 1
                else:
                    r = mid
            return r

        # k is too large, TLE

        # if k < neg_count:
        #     q = []
        #     if pos_y:
        #         for i, x in enumerate(neg_x):
        #             heappush(q, (x * pos_y[-1], x, len(pos_y) - 1, 1))
        #     if pos_x:
        #         for i, y in enumerate(neg_y):
        #             heappush(q, (y * pos_x[-1], y, len(pos_x) - 1, 0))

        #     for _ in range(k):
        #         _, x, i, flag = heappop(q)
        #         if i > 0:
        #             heappush(q, (x * pos[flag][i - 1], x, i - 1, flag))

        #     return q[0][0]

        # else:
        #     k -= neg_count
        #     q = []
        #     if pos_y:
        #         for i, x in enumerate(pos_x):
        #             heappush(q, (x * pos_y[0], x, 0, 1))
        #     if neg_y:
        #         for i, x in enumerate(neg_x):
        #             heappush(q, (x * neg_y[-1], x, len(neg_y) - 1, 0))

        #     for _ in range(k):
        #         _, x, i, flag = heappop(q)
        #         if flag:
        #             if i + 1 < len(pos_y):
        #                 heappush(q, (x * pos_y[i + 1], x, i + 1, flag))
        #         else:
        #             if i > 0:
        #                 heappush(q, (x * neg_y[i - 1], x, i - 1, flag))

        #     return q[0][0]


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallestProduct(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
