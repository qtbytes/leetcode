# Created by none at 2025/05/31 10:11
# leetgo: dev
# https://leetcode.com/problems/snakes-and-ladders/

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
    def snakesAndLadders(self, board: List[List[int]]) -> int | float:
        n = len(board)
        m = n * n
        dist = [inf] * m
        dist[0] = 0
        q = deque([0])
        while q:
            x = q.popleft()
            for y in range(x + 1, min(x + 7, m)):
                r, c = n - 1 - y // n, y % n
                if (n - 1 - r) & 1:
                    c = n - 1 - c
                if board[r][c] != -1:
                    y = board[r][c] - 1
                if dist[y] > dist[x] + 1:
                    dist[y] = dist[x] + 1
                    q.append(y)
        return -1 if dist[-1] == inf else dist[-1]


# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().snakesAndLadders(board)
    print("\noutput:", serialize(ans, "integer"))
