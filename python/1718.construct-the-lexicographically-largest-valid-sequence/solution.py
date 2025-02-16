# Created by none at 2025/02/16 15:32
# leetgo: 1.4.13
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

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


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        f = [0] * (2 * n - 1)

        def dfs(i: int):
            if i == len(f):
                return True
            if f[i] != 0:
                return dfs(i + 1)

            for num in reversed(range(1, n + 1)):
                if num not in f:
                    gap = 0 if num == 1 else num
                    if i + gap < len(f) and f[i] == f[i + gap] == 0:
                        f[i] = f[i + gap] = num
                        if dfs(i + 1):
                            return True
                        f[i] = f[i + gap] = 0

            return False

        dfs(0)
        return f


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().constructDistancedSequence(n)
    print("\noutput:", serialize(ans, "integer[]"))
