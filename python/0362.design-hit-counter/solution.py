# Created by none at 2025/05/15 15:58
# leetgo: 1.4.13
# https://leetcode.com/problems/design-hit-counter/

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
delay = 300


class HitCounter:
    def __init__(self):
        self.t = deque()

    def hit(self, timestamp: int) -> None:
        self.t.append(timestamp)
        while self.t[0] + delay < timestamp:
            self.t.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.t and self.t[0] + delay <= timestamp:
            self.t.popleft()
        return len(self.t)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = HitCounter()

    for i in range(1, len(ops)):
        match ops[i]:
            case "hit":
                method_params = split_array(params[i])
                timestamp: int = deserialize("int", method_params[0])
                obj.hit(timestamp)
                output.append("null")
            case "getHits":
                method_params = split_array(params[i])
                timestamp: int = deserialize("int", method_params[0])
                ans = serialize(obj.getHits(timestamp))
                output.append(ans)

    print("\noutput:", join_array(output))
