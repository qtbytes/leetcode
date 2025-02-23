# Created by none at 2025/02/23 13:41
# leetgo: 1.4.13
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        # construct root.left
        left = preorder[1]
        # size of root.left
        j = postorder.index(left) + 1
        root.left = self.constructFromPrePost(preorder[1 : 1 + j], postorder[:j])
        root.right = self.constructFromPrePost(
            preorder[1 + j :], postorder[j : len(postorder) - 1]
        )
        return root


# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().constructFromPrePost(preorder, postorder)
    print("\noutput:", serialize(ans, "TreeNode"))
