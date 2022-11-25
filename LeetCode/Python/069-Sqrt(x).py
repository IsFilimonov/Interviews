class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Do not use standard functions.
        Alternative: binary search with left, right and middle indexes.
        """
        i = 0
        while i*i <= x:
            i += 1

        return i-1


if __name__ == "__main__":
    s = Solution()

    tests = (
        (4, 2),
        (8, 2),
    )

    for test in tests:
        exec("assert s.mySqrt(test[0]) == test[1]")

    print("Well done!")
