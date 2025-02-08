# Created by none at 2025/02/08 14:24
# leetgo: 1.4.13
# https://leetcode.com/problems/design-a-number-container-system/

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


class NumberContainers:
    def __init__(self):
        self.map = {}
        self.indexs = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.map[index] = number
        heappush(self.indexs[number], (index, number))

    def find(self, number: int) -> int:
        h = self.indexs[number]

        # delay delete
        while h:
            i, v = h[0]
            if self.map[i] != v:
                heappop(h)
            else:
                break

        if not h:
            return -1
        return h[0][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = NumberContainers()

    for i in range(1, len(ops)):
        match ops[i]:
            case "change":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                number: int = deserialize("int", method_params[1])
                obj.change(index, number)
                output.append("null")
            case "find":
                method_params = split_array(params[i])
                number: int = deserialize("int", method_params[0])
                ans = serialize(obj.find(number))
                output.append(ans)

    print("\noutput:", join_array(output))
