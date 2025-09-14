# Created by none at 2025/09/14 10:12
# leetgo: dev
# https://leetcode.com/problems/vowel-spellchecker/

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


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_set = set(wordlist)
        word_lower_map = {}
        word_vowel_map = {}
        vowels = "aeiou"

        for i, word in enumerate(wordlist):
            w = word.lower()
            if w not in word_lower_map:
                word_lower_map[w] = i
            w = "".join([ch if ch not in vowels else " " for ch in w])
            if w not in word_vowel_map:
                word_vowel_map[w] = i

        def handle(w: str) -> str:
            if w in word_set:
                return w

            w = w.lower()
            if w in word_lower_map:
                return wordlist[word_lower_map[w]]

            w_vowel = "".join([ch if ch not in vowels else " " for ch in w])
            if w_vowel in word_vowel_map:
                return wordlist[word_vowel_map[w_vowel]]

            return ""

        return [handle(q) for q in queries]


# @lc code=end

if __name__ == "__main__":
    wordlist: List[str] = deserialize("List[str]", read_line())
    queries: List[str] = deserialize("List[str]", read_line())
    ans = Solution().spellchecker(wordlist, queries)
    print("\noutput:", serialize(ans, "string[]"))
