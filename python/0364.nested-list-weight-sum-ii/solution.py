# Created by none at 2025/05/13 13:58
# leetgo: 1.4.13
# https://leetcode.com/problems/nested-list-weight-sum-ii/

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

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def find_max_depth(ni: NestedInteger):
            if ni.isInteger():
                return 1
            return max((find_max_depth(sub) + 1) for sub in ni.getList())

        def dfs(ni: NestedInteger, depth: int):
            if ni.isInteger():
                return (max_depth + 1 - depth) * ni.getInteger()
            return sum(dfs(sub, depth + 1) for sub in ni.getList())

        max_depth = max(find_max_depth(ni) for ni in nestedList)
        return sum(dfs(ni, 1) for ni in nestedList)


# @lc code=end

if __name__ == "__main__":
    nestedList: List[NestedInteger] = deserialize("List[NestedInteger]", read_line())
    ans = Solution().depthSumInverse(nestedList)
    print("\noutput:", serialize(ans, "integer"))
