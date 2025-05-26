# Created by none at 2025/05/26 16:35
# leetgo: dev
# https://leetcode.com/problems/candy-crush/

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


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            stable = True

            for i in range(m):
                for j in range(n):
                    x = abs(board[i][j])
                    if x == 0:
                        continue

                    right = j
                    while right < n and abs(board[i][right]) == x:
                        right += 1
                        if right - j > 2:
                            stable = False
                            for k in range(j, right):
                                board[i][k] = -abs(board[i][k])
                            break

                    bottom = i
                    while bottom < m and abs(board[bottom][j]) == x:
                        bottom += 1
                        if bottom - i > 2:
                            stable = False
                            for k in range(i, bottom):
                                board[k][j] = -abs(board[k][j])
                            break

            if stable:
                return board

            for j in range(n):
                row = m - 1
                for i in range(m - 1, -1, -1):
                    while row >= 0 and board[row][j] < 0:
                        row -= 1
                    if row == -1:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[row][j]
                        row -= 1


# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().candyCrush(board)
    print("\noutput:", serialize(ans, "integer[][]"))
