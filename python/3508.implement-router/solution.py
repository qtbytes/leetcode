# Created by none at 2025/09/20 08:38
# leetgo: dev
# https://leetcode.com/problems/implement-router/

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


class Router:
    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.capacity = memoryLimit
        self.map = defaultdict(deque)
        self.packet = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        item = (source, destination, timestamp)
        if item in self.packet:
            return False
        self.map[destination].append(timestamp)
        self.q.append(item)
        self.packet.add(item)
        if len(self.q) > self.capacity:
            self.forwardPacket()
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        item = self.q.popleft()
        (_, destination, _) = item
        self.map[destination].popleft()
        self.packet.remove(item)
        return list(item)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        v = self.map[destination]
        l = bisect_left(v, startTime)
        r = bisect_right(v, endTime)
        return r - l


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    memoryLimit: int = deserialize("int", constructor_params[0])
    obj = Router(memoryLimit)

    for i in range(1, len(ops)):
        match ops[i]:
            case "addPacket":
                method_params = split_array(params[i])
                source: int = deserialize("int", method_params[0])
                destination: int = deserialize("int", method_params[1])
                timestamp: int = deserialize("int", method_params[2])
                ans = serialize(obj.addPacket(source, destination, timestamp))
                output.append(ans)
            case "forwardPacket":
                ans = serialize(obj.forwardPacket())
                output.append(ans)
            case "getCount":
                method_params = split_array(params[i])
                destination: int = deserialize("int", method_params[0])
                startTime: int = deserialize("int", method_params[1])
                endTime: int = deserialize("int", method_params[2])
                ans = serialize(obj.getCount(destination, startTime, endTime))
                output.append(ans)

    print("\noutput:", join_array(output))
