# Created by none at 2025/05/06 15:17
# leetgo: 1.4.13
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        q = deque([(root, 0)])

        def bfs(q: deque[tuple[TreeNode | None, int]]):
            while q:
                root, x = q.popleft()
                if not root:
                    continue
                res[x].append(root.val)
                q.append((root.left, x - 1))
                q.append((root.right, x + 1))

        bfs(q)

        return [res[x] for x in sorted(res)]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().verticalOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
