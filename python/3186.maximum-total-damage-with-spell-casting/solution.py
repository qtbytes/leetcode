# Created by none at 2025/10/11 09:31
# leetgo: dev
# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

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
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)

        spells = sorted(cnt)

        n = len(spells)

        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            s = spells[i]
            j = i + 1
            while j < n and spells[j] - s <= 2:
                j += 1
            op1 = s * cnt[s] + dfs(j)
            op2 = dfs(i + 1)
            return max(op1, op2)

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    power: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumTotalDamage(power)
    print("\noutput:", serialize(ans, "long"))
