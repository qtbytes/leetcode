# Created by none at 2024/12/23 15:12
# leetgo: 1.4.11
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        cur_level = [root]

        def f(nums: list[int]) -> int:
            mp = {v: i for i, v in enumerate(sorted(nums))}
            s = set()
            res = 0
            for x in nums:
                if x not in s:
                    # we find a circle, and only need replace `len(circle) - 1`  times
                    cnt = 0
                    while x not in s:
                        cnt += 1
                        s.add(x)
                        x = nums[mp[x]]
                    res += cnt - 1
            return res

        while cur_level:
            nxt_level = []
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)

            cur_level = nxt_level
            res += f([node.val for node in cur_level])

        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().minimumOperations(root)
    print("\noutput:", serialize(ans, "integer"))
