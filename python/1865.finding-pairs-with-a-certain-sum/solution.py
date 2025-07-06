# Created by none at 2025/07/06 09:35
# leetgo: dev
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import Iterable, List, Optional

from leetgo_py import *

# @lc code=begin


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.nums = nums2
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        origin = self.nums[index]
        self.nums[index] += val
        self.cnt2[origin] -= 1
        self.cnt2[origin + val] += 1

    def count(self, tot: int) -> int:
        res = 0
        for x, c1 in self.cnt1.items():
            res += c1 * (self.cnt2[tot - x])
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums1: List[int] = deserialize("List[int]", constructor_params[0])
    nums2: List[int] = deserialize("List[int]", constructor_params[1])
    obj = FindSumPairs(nums1, nums2)

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.add(index, val)
                output.append("null")
            case "count":
                method_params = split_array(params[i])
                tot: int = deserialize("int", method_params[0])
                ans = serialize(obj.count(tot))
                output.append(ans)

    print("\noutput:", join_array(output))
