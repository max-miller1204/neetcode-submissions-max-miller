class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: n = 0 or 1
        if n <= 2:
            return n

        # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)