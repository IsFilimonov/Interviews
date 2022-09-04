from typing import List


class Solution:
    def validate(self, nums: List[int]) -> None:
        assert 1 <= len(nums) <= 10**5
        assert all([-10**4 <= el <= 10**4 for el in nums])

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current = best = nums[0]
        for el in nums[1:]:
            current = max(el, current + el)
            best = max(best, current)

        return best

    # Time limit
    # def maxSubArray(self, nums: List[int]) -> int:
        # cs = s = sum(nums)
        # m = max(nums)
        # l = len(nums)

        # best = max(s,m)

        # for i in range(l):
        #     c = l
        #     if i > 0:
        #         cs = s - nums[i-1]

        #     while i < c:
        #         # if best < sum(nums[i:c]):
        #         if best < cs:
        #             best = cs
        #         else:
        #             cs -= nums[c-i-1]
        #         c -= 1

        # return best

    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


if __name__ == "__main__":
    s = Solution()

    tests = (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23)
    )

    for test in tests:
        exec("s.validate(test[0])")
        exec("s.maxSubArray(test[0])==test[1]")

    print("Well done!")
