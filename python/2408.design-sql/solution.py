# Created by none at 2025/05/23 15:41
# leetgo: dev
# https://leetcode.com/problems/design-sql/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.table = {}
        self.size = {}
        self.index = {}
        for name, column in zip(names, columns):
            self.table[name] = {}
            self.size[name] = column
            self.index[name] = 1

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.table or len(row) != self.size[name]:
            return False
        id = self.index[name]
        self.index[name] += 1
        self.table[name][id] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.table or rowId not in self.table[name]:
            return
        del self.table[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if (
            name not in self.table
            or rowId not in self.table[name]
            or columnId > len(self.table[name][rowId])
        ):
            return "<null>"
        return self.table[name][rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        res = []
        for rowId, column in self.table[name].items():
            res.append(str(rowId) + "," + ",".join(column))
        return res


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    names: list[str] = deserialize("List[str]", constructor_params[0])
    columns: list[int] = deserialize("List[int]", constructor_params[1])
    obj = SQL(names, columns)

    for i in range(1, len(ops)):
        match ops[i]:
            case "ins":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                row: List[str] = deserialize("List[str]", method_params[1])
                ans = serialize(obj.ins(name, row))
                output.append(ans)
            case "rmv":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                rowId: int = deserialize("int", method_params[1])
                obj.rmv(name, rowId)
                output.append("null")
            case "sel":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                rowId: int = deserialize("int", method_params[1])
                columnId: int = deserialize("int", method_params[2])
                ans = serialize(obj.sel(name, rowId, columnId))
                output.append(ans)
            case "exp":
                method_params = split_array(params[i])
                name: str = deserialize("str", method_params[0])
                ans = serialize(obj.exp(name))
                output.append(ans)

    print("\noutput:", join_array(output))
