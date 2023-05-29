class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        for i in range(1, n + 1):
            for possibility in range(1, maxPts + 1):
                dp[i] += dp[i - possibility] / maxPts

        for y in dp:
            print(y)
        return sum(dp[n][0:k + 1])


x = Solution()
print(x.new21Game(n=10, k=1, maxPts=10))
print(x.new21Game(n=6, k=1, maxPts=10))
print(x.new21Game(n=21, k=17, maxPts=10))
