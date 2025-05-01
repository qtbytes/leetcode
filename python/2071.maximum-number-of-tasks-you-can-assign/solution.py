# Created by none at 2025/05/01 12:32
# leetgo: 1.4.13
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

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
from sortedcontainers import SortedList


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def check(mid: int) -> bool:
            # only use workers[m-mid:]
            sl = SortedList(workers[m - mid :])
            pill_cnt = 0
            for i in range(mid - 1, -1, -1):
                if sl[-1] >= tasks[i]:
                    sl.pop()
                elif pill_cnt == pills:
                    return False
                else:
                    j = sl.bisect_left(tasks[i] - strength)
                    if j == len(sl):
                        return False
                    sl.pop(j)
                    pill_cnt += 1
            return True

        l = 0
        r = min(m, n)
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l


# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    workers: List[int] = deserialize("List[int]", read_line())
    pills: int = deserialize("int", read_line())
    strength: int = deserialize("int", read_line())
    ans = Solution().maxTaskAssign(tasks, workers, pills, strength)
    print("\noutput:", serialize(ans, "integer"))
