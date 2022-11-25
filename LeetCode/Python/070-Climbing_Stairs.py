class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Fibonacci
        """
        if n <= 3:
            return n

        step = (1, 2)
        for i in range(3, n+1):
            step = (step[1], step[0]+step[1])
        return step[-1]


if __name__ == "__main__":
    s = Solution()

    tests = (
        (2, 2),
        (3, 3),
    )

    for test in tests:
        exec("assert s.climbStairs(test[0]) == test[1]")

    print("Well done!")
