# Created by none at 2024/12/28 16:12
# leetgo: 1.4.11
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

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
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f = [[-inf] * (n + 1) for _ in range(3)]
        s = 0
        for i in range(n):
            s += nums[i]
            if i >= k - 1:
                f[0][i - (k - 1) + 1] = s
                s -= nums[i - (k - 1)]

        res = 0
        for t in range(1, 3):
            # f[t][i] = max(f[t][i-1], f[0][i] +max(f[t - 1][: i - k + 1]))
            g = f[t - 1].copy()
            for i in range(1, len(g)):
                g[i] = max(g[i], g[i - 1])
            for i in range(t * k, n + 1):
                f[t][i] = f[0][i] + g[i - k]
                if f[t][i] > f[t][res]:
                    res = i

        ans = [res]
        for i in range(2, 0, -1):
            total = f[i][res] - f[0][res]
            res = f[i - 1].index(total)
            ans.append(res)

        return [x - 1 for x in ans[::-1]]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSumOfThreeSubarrays(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
