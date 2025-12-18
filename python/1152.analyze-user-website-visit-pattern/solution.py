# Created by none at 2025/05/15 15:27
# leetgo: 1.4.13
# https://leetcode.com/problems/analyze-user-website-visit-pattern/

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
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        map = defaultdict(list)
        n = len(website)

        for i in sorted(range(n), key=lambda i: timestamp[i]):
            map[username[i]].append(website[i])

        cnt: defaultdict[str, int] = defaultdict(int)

        for v in map.values():
            n = len(v)
            if n < 3:
                continue
            seen = set()
            # can be replaced by builtin function
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = " ".join((v[i], v[j], v[k]))
                        if pattern not in seen:
                            seen.add(pattern)
                            cnt[pattern] += 1

        score = 0
        res = ""
        for pattern, c in cnt.items():
            if c > score or c == score and pattern < res:
                score = c
                res = pattern
        return res.split()


# @lc code=end

if __name__ == "__main__":
    username: List[str] = deserialize("List[str]", read_line())
    timestamp: List[int] = deserialize("List[int]", read_line())
    website: List[str] = deserialize("List[str]", read_line())
    ans = Solution().mostVisitedPattern(username, timestamp, website)
    print("\noutput:", serialize(ans, "string[]"))
