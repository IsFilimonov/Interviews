#!/usr/bin/env python
from typing import List


class Solution:
    """
    Test class
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        test
        """
        left, right = 0, len(nums) - 1

        if target < nums[left]:
            return 0
        if target > nums[right]:
            return right + 1

        middle = right // 2
        while right - left > 1:
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle
                middle = middle + (right-middle) // 2
            elif target < nums[middle]:
                right = middle
                middle = middle // 2

        return right if target > nums[left] else left


if __name__ == "__main__":
    s = Solution()

    tests = (
        (([3, 5, 7, 9, 10], 8), 3),
        (([1,3,4,5,6,7],2), 1),
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4),
        (([1,2,3], 4), 3),
        (([2,3,4], 1), 0),
    )

    for test in tests:
        exec("assert s.searchInsert(*test[0]) == test[1]")

    print("Well done!")
