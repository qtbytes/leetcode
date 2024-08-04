# Created by none at 2024/08/04 12:52
# leetgo: 1.4.7
# https://leetcode.cn/problems/subtree-of-another-tree/

from typing import *
from leetgo_py import *

import bisect
import collections
import functools
import heapq
import itertools
import operator
import math
import string

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (
                p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
            )

        def check(root):
            if not root:
                return False
            return is_same(root, subRoot) or check(root.left) or check(root.right)

        return check(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    subRoot: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSubtree(root, subRoot)
    print("\noutput:", serialize(ans, "boolean"))
