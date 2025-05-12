# Created by none at 2025/05/12 20:11
# leetgo: 1.4.13
# https://leetcode.com/problems/max-stack/

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
from sortedcontainers import SortedList


class MaxStack:
    def __init__(self):
        self.st = []
        self.sl = SortedList()

    def _remove_unvalid(self):
        while self.st[-1] is None:
            self.st.pop()

    def push(self, x: int) -> None:
        self.st.append(x)
        self.sl.add((x, len(self.st) - 1))

    def pop(self) -> int:
        self._remove_unvalid()
        x = self.st.pop()
        self.sl.remove((x, len(self.st)))
        return x

    def top(self) -> int:
        self._remove_unvalid()
        return self.st[-1]

    def peekMax(self) -> int:
        return self.sl[-1][0]

    def popMax(self) -> int:
        x, i = self.sl.pop()
        self.st[i] = None
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MaxStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                x: int = deserialize("int", method_params[0])
                obj.push(x)
                output.append("null")
            case "pop":
                ans = serialize(obj.pop())
                output.append(ans)
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "peekMax":
                ans = serialize(obj.peekMax())
                output.append(ans)
            case "popMax":
                ans = serialize(obj.popMax())
                output.append(ans)

    print("\noutput:", join_array(output))
