# Created by none at 2025/09/17 08:54
# leetgo: dev
# https://leetcode.com/problems/design-a-food-rating-system/

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


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.map = defaultdict(list)
        self.info = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.info[f] = (c, r)
            heappush(self.map[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.info[food]
        self.info[food] = (c, newRating)
        heappush(self.map[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        q = self.map[cuisine]  # priority queue
        while q:
            r, f = q[0]
            if self.info[f][1] != -r:
                heappop(q)
                continue
            return f
        raise NotImplementedError


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    foods: List[str] = deserialize("List[str]", constructor_params[0])
    cuisines: List[str] = deserialize("List[str]", constructor_params[1])
    ratings: List[int] = deserialize("List[int]", constructor_params[2])
    obj = FoodRatings(foods, cuisines, ratings)

    for i in range(1, len(ops)):
        match ops[i]:
            case "changeRating":
                method_params = split_array(params[i])
                food: str = deserialize("str", method_params[0])
                newRating: int = deserialize("int", method_params[1])
                obj.changeRating(food, newRating)
                output.append("null")
            case "highestRated":
                method_params = split_array(params[i])
                cuisine: str = deserialize("str", method_params[0])
                ans = serialize(obj.highestRated(cuisine))
                output.append(ans)

    print("\noutput:", join_array(output))
