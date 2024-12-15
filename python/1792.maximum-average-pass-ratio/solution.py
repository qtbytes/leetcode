# Created by none at 2024/12/15 14:22
# leetgo: 1.4.9
# https://leetcode.com/problems/maximum-average-pass-ratio/

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


class PassRatio:
    def __init__(self, p: int, total: int):
        self.p = p
        self.total = total

    def __str__(self):
        return f"{self.p} {self.total}"

    def __lt__(self, other: "PassRatio"):
        # python heap is min heap
        # here we want (a+1)/(b+1) - (a/b) maxium
        return (self.total - self.p) * (other.total * (other.total + 1)) >= (
            other.total - other.p
        ) * (self.total * (self.total + 1))


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for p, t in classes:
            heappush(q, PassRatio(p, t))
        for _ in range(extraStudents):
            pr = heappop(q)
            heappush(q, PassRatio(pr.p + 1, pr.total + 1))
        return sum(pr.p / pr.total for pr in q) / len(q)


# @lc code=end

if __name__ == "__main__":
    classes: List[List[int]] = deserialize("List[List[int]]", read_line())
    extraStudents: int = deserialize("int", read_line())
    ans = Solution().maxAverageRatio(classes, extraStudents)
    print("\noutput:", serialize(ans, "double"))
