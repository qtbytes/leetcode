# Created by none at 2025/05/23 16:39
# leetgo: dev
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

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


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, next: "Node" | None = None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal: int) -> "Node":
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        # all node is equal
        p = head.next
        while p is not head and p.val == head.val:
            p = p.next
        if p is head:
            head.next = Node(insertVal, head.next)
            return head

        # value is min or max
        while p.val <= p.next.val:
            p = p.next
        if insertVal >= p.val or insertVal <= p.next.val:
            p.next = Node(insertVal, p.next)
            return head

        # normal situaion: find the last node <= insertVal
        while p.next.val <= insertVal:
            p = p.next
        p.next = Node(insertVal, p.next)
        return head


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    insertVal: int = deserialize("int", read_line())
    ans = Solution().insert(head, insertVal)
    print("\noutput:", serialize(ans, "ListNode"))
