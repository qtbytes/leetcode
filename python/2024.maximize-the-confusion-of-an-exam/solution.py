# Created by none at 2024/09/02 11:43
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/

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

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def f(s:str, target:str, k:int):
            l = 0
            res = 0
            for r, ch in enumerate(s):
                while ch != target and k == 0:
                    k += s[l] != target
                    l += 1
                res = max(res,r - l + 1 )
                if ch != target:
                    k -= 1
            return res
        return max(f(answerKey, "T", k), f(answerKey, 'F', k))


# @lc code=end

if __name__ == "__main__":
    answerKey: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxConsecutiveAnswers(answerKey, k)
    print("\noutput:", serialize(ans, "integer"))
