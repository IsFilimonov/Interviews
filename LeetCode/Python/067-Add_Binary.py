from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Drop prefix 0b
        """
        return bin(int(a, base=2) + int(b, base=2))[2:]


if __name__ == "__main__":
    s = Solution()

    tests = (
        (("11", "1"), "100"),
        (("1010", "1011"), "10101"),

    )

    for test in tests:
        exec("assert s.addBinary(*test[0]) == test[1]")

    print("Well done!")
