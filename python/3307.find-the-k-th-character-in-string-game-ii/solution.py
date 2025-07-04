# Created by none at 2025/07/04 08:46
# leetgo: dev
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

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


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1

        def f(k: int):
            if k == 0:
                return 0
            n = k.bit_length()
            i = n - 1
            return (operations[i] + f(k % (1 << i))) % 26

        return chr(ord("a") + f(k))


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    operations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().kthCharacter(k, operations)
    print("\noutput:", serialize(ans, "character"))
