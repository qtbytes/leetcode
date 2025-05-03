# Created by none at 2025/05/03 23:06
# leetgo: 1.4.13
# https://leetcode.com/problems/design-in-memory-file-system/

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


class FileSystem:
    def __init__(self):
        self.map = {}

    def cd(self, path: str) -> dict:
        root = self.map
        for dir in path.split("/"):
            if dir:
                if dir not in root:
                    root[dir] = dict()
                root = root[dir]
        return root

    @staticmethod
    def split(filePath: str):
        i = filePath.rfind("/")
        return filePath[:i], filePath[i + 1 :]

    def ls(self, path: str) -> List[str]:
        root = self.cd(path)
        if isinstance(root, dict):
            return sorted(root)
        return [path.split("/")[-1]]

    def mkdir(self, path: str) -> None:
        self.cd(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path, file_name = self.split(filePath)
        root = self.cd(path)
        if file_name not in root:
            root[file_name] = ""
        root[file_name] += content

    def readContentFromFile(self, filePath: str) -> str:
        path, file_name = self.split(filePath)
        root = self.cd(path)
        return root.get(file_name, "")


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FileSystem()

    for i in range(1, len(ops)):
        match ops[i]:
            case "ls":
                method_params = split_array(params[i])
                path: str = deserialize("str", method_params[0])
                ans = serialize(obj.ls(path))
                output.append(ans)
            case "mkdir":
                method_params = split_array(params[i])
                path: str = deserialize("str", method_params[0])
                obj.mkdir(path)
                output.append("null")
            case "addContentToFile":
                method_params = split_array(params[i])
                filePath: str = deserialize("str", method_params[0])
                content: str = deserialize("str", method_params[1])
                obj.addContentToFile(filePath, content)
                output.append("null")
            case "readContentFromFile":
                method_params = split_array(params[i])
                filePath: str = deserialize("str", method_params[0])
                ans = serialize(obj.readContentFromFile(filePath))
                output.append(ans)

    print("\noutput:", join_array(output))
