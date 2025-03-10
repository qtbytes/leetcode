# Created by none at 2025/03/10 13:47
# leetgo: 1.4.13
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

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


def atLeast(s: str, k: int) -> int:
    """At least contain k consonants"""
    n = len(s)
    r = 0
    res = 0
    vowels = defaultdict(int)
    consonants = 0
    for l in range(n):
        while r < n and (consonants < k or len(vowels) < 5):
            if s[r] in "aeiou":
                vowels[s[r]] += 1
            else:
                consonants += 1
            r += 1
        if consonants >= k and len(vowels) == 5:
            res += n - r + 1
        if s[l] in "aeiou":
            vowels[s[l]] -= 1
            if vowels[s[l]] == 0:
                del vowels[s[l]]
        else:
            consonants -= 1
    return res


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return atLeast(word, k) - atLeast(word, k + 1)


"""         
        vowels = set("aeiou")
        lastIndex = defaultdict(deque)
        consonants = deque()
        res = 0
        l = 0
        for r, ch in enumerate(word):
            if ch in vowels:
                lastIndex[ch].append(r)
            else:
                consonants.append(r)
                while l <= r and len(consonants) > k:
                    if word[l] in vowels:
                        lastIndex[word[l]].popleft()
                        if not lastIndex[word[l]]:
                            del lastIndex[word[l]]
                    else:
                        consonants.popleft()
                    l += 1

            if len(consonants) == k and len(lastIndex) == 5:
                x, y = inf, inf
                for v in lastIndex.values():
                    x = min(v[0], x)
                    y = min(v[-1], y)
                if consonants:
                    x = min(consonants[0], x)
                    y = min(consonants[0], y)
                # print(r, y, x)
                res += max(0, y - x + 1)

        return res
 """


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countOfSubstrings(word, k)
    print("\noutput:", serialize(ans, "long"))
