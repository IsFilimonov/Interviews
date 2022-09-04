from typing import List


class Solution:
    def validate(self, nums: List[int]) -> None:
        assert 1 <= len(nums) <= 3 * 10 ** 4
        assert all([-100 <= el <= 100 for el in nums])
        # nums is sorted in non-decreasing order.

    def removeDuplicates(self, nums: List[int]) -> int:
        count, shift, unique = 0, 0, None

        for i in range(len(nums)):
            if nums[i] != unique:
                # Unique value
                count += 1
                nums[i-shift] = unique = nums[i]
            else:
                # Dublicate
                shift += 1

        del shift, unique
        return count


if __name__ == "__main__":
    s = Solution()

    tests = (
        ([1, 1, 1, 2, 2, 3, 3, 4], 4),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    )

    for test in tests:
        exec("assert s.removeDuplicates(test[0]) == test[1]")

    print("Well done!")
