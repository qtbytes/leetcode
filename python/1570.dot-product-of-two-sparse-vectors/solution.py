# Created by none at 2025/05/06 15:49
# leetgo: 1.4.13
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

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


class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {i: x for i, x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        return sum(self.map[i] * vec.map[i] for i in self.map.keys() & vec.map.keys())


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    v1: List[int] = deserialize("List[int]", read_line())
    v2: List[int] = deserialize("List[int]", read_line())
    ans = SparseVector(v1).dotProduct(SparseVector(v2))
    print("\noutput:", serialize(ans, "integer"))
