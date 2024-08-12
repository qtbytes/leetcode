# Created by none at 2024/08/12 13:05
# leetgo: 1.4.7
# https://leetcode.cn/problems/implement-magic-dictionary/

from typing import *
from leetgo_py import *

import bisect
import collections
import functools
import heapq
import itertools
import operator
import math
import string

# @lc code=begin


class MagicDictionary:
    def __init__(self):
        self.mp = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.mp[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.mp:
            return False
        return any(
            sum(x != y for x, y in zip(searchWord, word)) == 1 for word in self.mp[n]
        )


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MagicDictionary()

    for i in range(1, len(ops)):
        match ops[i]:
            case "buildDict":
                method_params = split_array(params[i])
                dictionary: List[str] = deserialize("List[str]", method_params[0])
                obj.buildDict(dictionary)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                searchWord: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(searchWord))
                output.append(ans)

    print("\noutput:", join_array(output))
