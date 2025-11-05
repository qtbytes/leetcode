# Created by none at 2025/11/05 10:53
# leetgo: dev
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

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
from sortedcontainers import SortedDict, SortedList


class Solution:
    def findXSum(self, nums: List[int], size: int, topK: int) -> List[int]:
        maxFreq = SortedList()
        cnt = defaultdict(int)
        s = 0

        def add(x):
            nonlocal s
            # remove old freq of x
            if cnt[x] > 0:
                i = maxFreq.bisect_left((cnt[x], x))
                # x is topK
                if len(maxFreq) - i <= topK:
                    s -= x * cnt[x]
                    j = len(maxFreq) - topK - 1
                    if j >= 0:
                        add_freq, add_x = maxFreq[j]
                        s += add_x * add_freq
                maxFreq.remove((cnt[x], x))
            # add new freq of x
            cnt[x] += 1
            maxFreq.add((cnt[x], x))
            i = maxFreq.bisect_left((cnt[x], x))
            if len(maxFreq) - i <= topK:
                s += x * cnt[x]
                j = len(maxFreq) - topK - 1
                if j >= 0:
                    del_freq, del_x = maxFreq[j]
                    s -= del_x * del_freq

        def remove(x):
            nonlocal s
            # maintain maxfreq
            i = maxFreq.bisect_left((cnt[x], x))
            if len(maxFreq) - i <= topK:
                s -= x * cnt[x]
                j = len(maxFreq) - topK - 1
                if j >= 0:
                    add_freq, add_x = maxFreq[j]
                    s += add_x * add_freq
            maxFreq.remove((cnt[x], x))
            cnt[x] -= 1
            if cnt[x] > 0:
                maxFreq.add((cnt[x], x))
                i = maxFreq.bisect_left((cnt[x], x))
                if len(maxFreq) - i <= topK:
                    s += x * cnt[x]
                    j = len(maxFreq) - topK - 1
                    if j >= 0:
                        del_freq, del_x = maxFreq[j]
                        s -= del_x * del_freq

        for i in range(size - 1):
            add(nums[i])

        res = []
        for i in range(size - 1, len(nums)):
            add(nums[i])
            res.append(s)
            remove(nums[i - (size - 1)])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findXSum(nums, k, x)
    print("\noutput:", serialize(ans, "long[]"))
