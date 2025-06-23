# Created by none at 2025/06/23 12:53
# leetgo: dev
# https://leetcode.com/problems/sum-of-k-mirror-numbers/

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
def to_base(x: int, k: int):
    res = []
    while x:
        res.append(str(x % k))
        x //= k
    return "".join(res[::-1])


def is_mirror(s: str):
    return s == s[::-1]


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        q = []

        def check_add(q: list[int], x: int) -> bool:
            q.append(x)
            # print(x, end=" ")
            # print(len(q), end=" ")
            return len(q) < n

        for x in range(1, 10):
            if is_mirror(to_base(x, k)):
                if not check_add(q, x):
                    return sum(q)

        nums = [pow(10, i) for i in range(6)]

        for left in range(1, int(2e5)):
            if left in nums:
                i = nums.index(left)
                for l in range(nums[i - 1], nums[i]):
                    l = str(l)
                    for mid in range(10):
                        x = int(l + str(mid) + l[::-1])
                        if is_mirror(to_base(x, k)):
                            if not check_add(q, x):
                                return sum(q)

            left = str(left)
            x = int(left + left[::-1])
            if is_mirror(to_base(x, k)):
                if not check_add(q, x):
                    return sum(q)
        return -1


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().kMirror(k, n)
    print("\noutput:", serialize(ans, "long"))
