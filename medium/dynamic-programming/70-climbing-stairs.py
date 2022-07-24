class Solution:
    def __init__(self):
        self.memo = []

    def helper(self, n: int) -> int:
        if n == 2:
            return 2
        elif n == 1:
            return 1
        elif n == 0:
            return 0

        if self.memo[n] > 0:
            return self.memo[n]

        self.memo[n-1] = self.helper(n-1)
        self.memo[n-2] = self.helper(n-2)

        return self.memo[n-1] + self.memo[n-2]

    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n + 1)
        return self.helper(n)


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
