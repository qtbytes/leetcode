# Created by none at 2025/02/14 23:03
# leetgo: 1.4.13
# https://leetcode.com/problems/product-of-the-last-k-numbers/

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


class ProductOfNumbers:
    def __init__(self):
        self.p = [1]
        self.s = 1
        self.zero = -1

    def add(self, num: int) -> None:
        self.s *= num
        if num == 0:
            self.zero = len(self.p)
            self.s = 1  # ignore zero
        self.p.append(self.s)

    def getProduct(self, k: int) -> int:
        n = len(self.p)
        # print(self.p)
        if n - k <= self.zero:
            return 0
        return self.s // self.p[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = ProductOfNumbers()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.add(num)
                output.append("null")
            case "getProduct":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                ans = serialize(obj.getProduct(k))
                output.append(ans)

    print("\noutput:", join_array(output))
