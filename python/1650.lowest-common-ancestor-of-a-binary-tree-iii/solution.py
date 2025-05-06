# Created by none at 2025/05/06 15:38
# leetgo: 1.4.13
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

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


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# @lc code=begin


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        a, b = p, q

        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p

        return a


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: List[int] = deserialize("List[int]", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
