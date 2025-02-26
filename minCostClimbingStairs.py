class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        dp = [0] * n
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for i in range(n-3, -1, -1):
            one_step = (cost[i]+ dp[i+1]) 
            two_steps = (cost[i]+ dp[i+2]) 
            dp[i] = min(one_step, two_steps)
        return min(dp[0], dp[1])
        