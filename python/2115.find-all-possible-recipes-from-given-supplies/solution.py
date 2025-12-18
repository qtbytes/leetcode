# Created by none at 2025/03/21 11:49
# leetgo: 1.4.13
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

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
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        map = {
            recipe: set(ingredient) for recipe, ingredient in zip(recipes, ingredients)
        }
        supplies: set[str] = set(supplies)
        can = {}

        def can_make(recipe: str):
            can[recipe] = False
            for ingredient in map[recipe]:
                if ingredient not in supplies:
                    if ingredient not in map:
                        return False
                    if ingredient in can and not can[ingredient]:
                        return False
                    if not can_make(ingredient):
                        return False
            can[recipe] = True
            return True

        return [recipe for recipe in recipes if can_make(recipe)]


# @lc code=end

if __name__ == "__main__":
    recipes: List[str] = deserialize("List[str]", read_line())
    ingredients: List[List[str]] = deserialize("List[List[str]]", read_line())
    supplies: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findAllRecipes(recipes, ingredients, supplies)
    print("\noutput:", serialize(ans, "string[]"))
