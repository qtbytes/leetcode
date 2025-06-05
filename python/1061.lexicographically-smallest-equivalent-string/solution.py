# Created by none at 2025/06/05 10:08
# leetgo: dev
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

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


def merge(s1: str, s2: str) -> dict[str, str]:
    fa = list(range(26))

    def find(x: int):
        if fa[x] != x:
            fa[x] = find(fa[x])
        return fa[x]

    def union(x: int, y: int):
        fx, fy = find(x), find(y)
        fa[fy] = fx

    for x, y in zip(s1, s2):
        union(ord(x) - ord("a"), ord(y) - ord("a"))

    groups = defaultdict(list)
    for i in range(26):
        groups[chr(find(i) + ord("a"))].append(chr(i + ord("a")))

    for g in groups:
        groups[g].sort()

    return {ch: g[0] for g in groups.values() for ch in g}

    # mp1 = defaultdict(list)
    # mp2 = defaultdict(list)
    # for i, ch in enumerate(s1):
    #     mp1[ch].append(i)
    # for i, ch in enumerate(s2):
    #     mp2[ch].append(i)

    # res = {ch: ch for ch in ascii_lowercase}

    # for i, ch in enumerate(s1):
    #     if not mp1[ch]:
    #         continue
    #     group = {ch}
    #     q = deque([i])
    #     while q:
    #         i = q.popleft()
    #         for equivalent in (s1[i], s2[i]):
    #             group.add(equivalent)
    #             q.extend(mp1[equivalent])
    #             q.extend(mp2[equivalent])
    #             del mp1[equivalent]
    #             del mp2[equivalent]
    #         # print(q)
    #     # print(group)

    #     mn = min(group)
    #     for key in group:
    #         res[key] = mn

    # return res


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = merge(s1, s2)
        return "".join(d[ch] for ch in baseStr)


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    baseStr: str = deserialize("str", read_line())
    ans = Solution().smallestEquivalentString(s1, s2, baseStr)
    print("\noutput:", serialize(ans, "string"))
