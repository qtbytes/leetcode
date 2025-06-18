# Created by none at 2025/06/18 16:26
# leetgo: dev
# https://leetcode.com/problems/find-median-from-data-stream/

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


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        heappush(self.min_heap, num)
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if self.n > 1 and self.min_heap[0] < -self.max_heap[0]:
            heappush(self.min_heap, -heappop(self.max_heap))
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if self.n & 1:
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MedianFinder()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addNum(num)
                output.append("null")
            case "findMedian":
                ans = serialize(obj.findMedian())
                output.append(ans)

    print("\noutput:", join_array(output))
