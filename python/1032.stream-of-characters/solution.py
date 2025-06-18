# Created by none at 2025/06/18 15:34
# leetgo: dev
# https://leetcode.com/problems/stream-of-characters/

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
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, w: Iterable):
        root = self.root
        for ch in w:
            if ch not in root:
                root[ch] = {}
            root = root[ch]
        root["#"] = True

    def contains(self, w: Iterable):
        root = self.root
        for ch in w:
            if "#" in root:
                return True
            if ch not in root:
                return False
            root = root[ch]
        return "#" in root


class StreamChecker:
    def __init__(self, words: List[str]):
        self.tree = Trie()
        self.max_len = 0
        for w in words:
            self.tree.add(w[::-1])
            self.max_len = max(self.max_len, len(w))

        self.q = deque()

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        if len(self.q) > self.max_len:
            self.q.pop()
        return self.tree.contains(self.q)


# BASE = 31
# MOD1 = 10**9 + 7
# MOD2 = 10**9 + 9


# def hash(s: str, mod: int, base: int = BASE) -> int:
#     res = 0
#     for i, ch in enumerate(s):
#         res = (res * base + ord(ch) - ord("a")) % mod
#     return res


# class StreamChecker:
#     def __init__(self, words: List[str]):
#         self.max_size = defaultdict(int)
#         self.words = defaultdict(set)
#         for w in words:
#             self.words[w[-1]].add((hash(w[::-1], mod=MOD1), hash(w[::-1], mod=MOD2)))
#             if (size := len(w)) > self.max_size[w[-1]]:
#                 self.max_size[w[-1]] = size

#         self.q = deque()

#     def query(self, letter: str) -> bool:
#         self.q.appendleft(letter)
#         s1 = s2 = 0
#         for i in range(min(self.max_size[letter], len(self.q))):
#             s1 = (s1 * BASE + ord(self.q[i]) - ord("a")) % MOD1
#             s2 = (s2 * BASE + ord(self.q[i]) - ord("a")) % MOD2
#             if (s1, s2) in self.words[letter]:
#                 return True
#         return False


# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    words: List[str] = deserialize("List[str]", constructor_params[0])
    obj = StreamChecker(words)

    for i in range(1, len(ops)):
        match ops[i]:
            case "query":
                method_params = split_array(params[i])
                letter: str = deserialize("str", method_params[0])
                ans = serialize(obj.query(letter))
                output.append(ans)

    print("\noutput:", join_array(output))
