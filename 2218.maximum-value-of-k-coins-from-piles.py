#
# @lc app=leetcode id=2218 lang=python3
#
# [2218] Maximum Value of K Coins From Piles
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i, coin_to_collect):
            '''
            @param:
                i :  choose only the pile starting from i 
            '''
            if i == len(piles) or coin_to_collect == 0:
                return 0
            ret, curr = dp(i+1, coin_to_collect), 0

            for _i, x in enumerate(piles[i]):
                if coin_to_collect-1-_i < 0:
                    break
                curr += x
                ret = max(dp(i+1, coin_to_collect-(_i + 1)) + curr, ret)
            return ret
        return dp(0, k)

# @lc code=end
