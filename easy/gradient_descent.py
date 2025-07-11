class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for _ in range(iterations):
            x -= learning_rate * (2 * x)

        return round(x, 5)


solution = Solution()

assert solution.get_minimizer(0, 0.01, 5) == 5
assert solution.get_minimizer(10, 0.01, 5) == 4.08536
