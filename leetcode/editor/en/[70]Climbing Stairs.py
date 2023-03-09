# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
# 
#  Related Topics Math Dynamic Programming Memoization 👍 17327 👎 535


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. dp array: ways to step up, index: ways to climb to ith floor
        # 2. function: dp[i] = dp[i-1] + dp[i-2] (i >= 1)
        # 3. init: dp[1] = 1, dp[2] = 2
        # 4. order: left to right
        # 5. eg: 1, 2, 3, 5, 8
        # rationale: to get to dp[i], you can either step one more step of 2 stairs from each of the way of dp[i-2], or step two more steps of 1 stair from each of the way of dp[i-1]
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

        
# leetcode submit region end(Prohibit modification and deletion)
