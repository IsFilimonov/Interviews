from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        All numbers map to str => join (only str) => to int + 1 => list comprehension to int
        """
        return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]


if __name__ == "__main__":
    s = Solution()

    tests = (
        ([1,2,3], [1,2,4]),
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    )

    for test in tests:
        exec("assert s.plusOne(test[0]) == test[1]")

    print("Well done!")
