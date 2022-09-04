import timeit
from typing import List
import random


class Solution(object):
    def __init__(self, list_length: tuple, list_values: tuple, int_value: tuple) -> None:  # PEP-0484
        self.nums = [random.randint(*list_values) for _ in range(random.randint(*list_length))]
        self.target = random.randint(*int_value)

    # Approach 1: Brute Force
    # Моё решение
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:], start=i+1):
                if v1 + v2 == target:
                    return [i, j]
        return ["no", "solution"]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    # Самое популярное решение
    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     #n^2
    #     ls = len(nums)
    #     for i in range(ls):
    #         for j in range(i + 1, ls):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # def twoSum(self, nums, target):
    #     # hash 1
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         try:
    #             hash_nums[num].append(index)
    #         except KeyError:
    #             hash_nums[num] = [index]
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             candicate = hash_nums[another]
    #             if another == num:
    #                 if len(candicate) > 1:
    #                     return candicate
    #                 else:
    #                     continue
    #             else:
    #                 return [index, candicate[0]]
    #         except KeyError:
    #             pass

    # def twoSum(self, nums, target):
    #     # hash 2
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             hash_nums[another]
    #             return [hash_nums[another], index]
    #         except KeyError:
    #             hash_nums[num] = index


if __name__ == '__main__':
    nums_length = (2, 50)# (2, 10**3)
    nums_values = (-10**9, 10**9)
    target_value = (-10**9, 10**9)

    s = Solution(nums_length, nums_values, target_value)
    # x = s.twoSum_3(s.nums, s.target)

    # t = timeit.Timer(lambda: s.twoSum_1(s.nums, s.target))
    # print(t.timeit())

    print(s.twoSum_3(nums=[2, 7, 11, 15], target=9))
    print(s.twoSum_3(nums=[3,2,4], target=6))
    print(s.twoSum_3(nums=[3,3], target=6))
