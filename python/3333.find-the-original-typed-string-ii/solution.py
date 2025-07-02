# Created by none at 2025/07/02 15:02
# leetgo: dev
# https://leetcode.com/problems/find-the-original-typed-string-ii/

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
mod = 10**9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        group = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1
            # each group need at least keep 1 char
            k -= 1
            # you can only operate group with size > 1
            if j - i > 1:
                group.append(j - i - 1)
            i = j

        """
        # if want select >= k char from group, hard
        def dfs(i: int, k: int) -> int:
            if i == len(group):
                return 0 if k > 0 else 1
            res = 0
            if k <= 0:
                return (group[i] + 1) * dfs(i + 1, 0) % mod
            for c in range(group[i] + 1):
                res = (res + dfs(i + 1, max(k - c, 0))) % mod
            return res

        return dfs(0, k)
        """

        # we select < k char from group, better
        total = 1
        for x in group:
            total = total * (x + 1) % mod
        if k <= 0:
            return total
        """
        f[i][j] = sum(f[i-1][j-c] for c in range(min(nums[i],j)+1))
                  p=j-c 
                = sum(f[i-1][p] for p in range(max(0, j-nums[i]), j+1))
        """

        f = [[0] * k for _ in range(len(group) + 1)]
        f[0] = [1] * k

        for i, x in enumerate(group, 1):
            s = list(accumulate(f[i - 1], initial=0))
            for j in range(k):
                f[i][j] = (s[j + 1] - s[max(0, j - x)]) % mod

        # print(f[-1])
        return (total - f[-1][-1]) % mod


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().possibleStringCount(word, k)
    print("\noutput:", serialize(ans, "integer"))
