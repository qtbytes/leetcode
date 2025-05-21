# Created by none at 2025/05/21 16:43
# leetgo: dev
# https://leetcode.com/problems/design-tic-tac-toe/

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


class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = self.antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1
        self.row[row] += value
        self.col[col] += value
        if row == col:
            self.diag += value
        if row + col == self.n - 1:
            self.antidiag += value
        q = (self.row[row], self.col[col], self.diag, self.antidiag)
        if self.n in q or -self.n in q:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = TicTacToe(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "move":
                method_params = split_array(params[i])
                row: int = deserialize("int", method_params[0])
                col: int = deserialize("int", method_params[1])
                player: int = deserialize("int", method_params[2])
                ans = serialize(obj.move(row, col, player))
                output.append(ans)

    print("\noutput:", join_array(output))
