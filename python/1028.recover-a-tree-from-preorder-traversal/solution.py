# Created by none at 2025/02/22 12:29
# leetgo: 1.4.13
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

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


class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        i = s.find("-")
        if i == -1:
            return TreeNode(int(s))

        st = []
        st.append((TreeNode(int(s[:i])), 0))
        n = len(s)
        while i < n:
            j = i + 1
            while j < n and s[j] == "-":
                j += 1
            depth = j - i
            i = j + 1
            while i < n and s[i].isdigit():
                i += 1
            val = int(s[j:i])
            # print(val, depth)

            while st:
                root, d = st[-1]
                if depth == d + 1:
                    if not root.left:
                        root.left = TreeNode(val)
                        st.append((root.left, depth))
                    else:
                        root.right = TreeNode(val)
                        st.append((root.right, depth))

                    break
                else:
                    st.pop()
            # print(st)
        return st[0][0]


# @lc code=end

if __name__ == "__main__":
    traversal: str = deserialize("str", read_line())
    ans = Solution().recoverFromPreorder(traversal)
    print("\noutput:", serialize(ans, "TreeNode"))
