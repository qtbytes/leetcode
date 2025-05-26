# Created by none at 2025/05/26 17:01
# leetgo: dev
# https://leetcode.com/problems/group-shifted-strings/

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, groupby, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

from leetgo_py import *

# @lc code=begin


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hash(key: str):
            return tuple((ord(y) - ord(x)) % 26 for x, y in pairwise(key))

        group = defaultdict(list)
        for s in strings:
            group[hash(s)].append(s)
        return list(group.values())


# @lc code=end

if __name__ == "__main__":
    strings: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupStrings(strings)
    print("\noutput:", serialize(ans, "string[][]"))
