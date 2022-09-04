from typing import (List,)


class Solution:
    def validate(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        assert len(nums1) == m+n
        assert len(nums2) == n
        assert (0 <= m <= 200) and (0 <= n <= 200) and (1 <= m+n <= 200)
        if m > 0:
            assert any([-109 <= el <= 109 for el in nums1])
        if n > 0:
            assert any([-109 <= el <= 109 for el in nums2])

    def merge(self, M: List[int], m: int, N: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if N[n-1] >= M[m-1]:
                M[m+n-1] = N[n-1]
                n -= 1
            else:
                M[m+n-1] = M[m-1]
                # M[m-1] = N[n-1]  # needs to collect all zeros from M to N
                m -= 1

        if n > 0:
            M[:n] = N[:n]
            return M

        return M


if __name__ == "__main__":
    s = Solution()

    tests = [
        # ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        # ([1], 1, [], 0, [1]),
        # ([0], 0, [1], 1, [1]),
        ([1, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 1, 3, 4, 5, 6])
    ]

    for test in tests:
        exec("s.validate(*test[:4])")
        exec("assert s.merge(*test[:4]) == test[4]")

    print("well done1")
