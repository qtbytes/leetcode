# Created by none at 2025/06/16 22:56
# leetgo: dev
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(root: TreeNode | None) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal ans
            ans = max(ans, root.val + max(left, 0) + max(right, 0))
            return root.val + max(left, right, 0)

        dfs(root)

        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxPathSum(root)
    print("\noutput:", serialize(ans, "integer"))
