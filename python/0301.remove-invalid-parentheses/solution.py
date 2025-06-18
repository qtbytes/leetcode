# Created by none at 2025/06/18 16:38
# leetgo: dev
# https://leetcode.com/problems/remove-invalid-parentheses/

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


def valid(s: Iterable) -> bool:
    bal = 0
    for ch in s:
        if ch not in "()":
            continue
        bal += 1 if ch == "(" else -1
        if bal < 0:
            return False
    return bal == 0


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        balance = 0
        cnt = 0
        nums = []
        for i, ch in enumerate(s):
            if ch in "()":
                nums.append(i)
                balance += 1 if ch == "(" else -1
                if balance < 0:
                    cnt += 1
                    balance = 0
        # we need remove balance `(`, cnt `)`
        total = balance + cnt
        res = []

        for mask in range(1 << len(nums)):
            if mask.bit_count() != total:
                continue
            t = list(s)
            a = [balance, cnt]
            for d, i in enumerate(nums):
                if mask >> d & 1:
                    a[t[i] == ")"] -= 1
                    t[i] = ""
            t = "".join(t)
            if a == [0, 0] and valid(t):
                res.append(t)
        return list(set(res))

        # res = []
        # path = []

        # def valid():
        #     balance = 0
        #     for ch in path:
        #         if ch in "()":
        #             balance += 1 if ch == "(" else -1
        #             if balance < 0:
        #                 return False
        #     return True

        # def dfs(i: int, left: int, right: int):
        #     if i == len(s):
        #         if left == 0 and right == 0 and valid():
        #             res.append("".join(path))
        #         return
        #     if s[i] not in "()":
        #         path.append(s[i])
        #         dfs(i + 1, left, right)
        #         path.pop()
        #         return
        #     # don't delete parentheses
        #     path.append(s[i])
        #     dfs(i + 1, left, right)
        #     path.pop()

        #     # delete left parenthese
        #     if s[i] == "(" and left > 0:
        #         dfs(i + 1, left - 1, right)

        #     # delete right parenthese
        #     if s[i] == ")" and right > 0:
        #         dfs(i + 1, left, right - 1)

        # dfs(0, balance, cnt)
        # return list(set(res))


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeInvalidParentheses(s)
    print("\noutput:", serialize(ans, "string[]"))
