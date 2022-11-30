from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy on lower, sell on higher.
        Min and max index does not the way. Set() also doesn't.
        Need to loop from left to right board, so you don't get index error.
        If we fond number smaller than left we jump to its. (left=right).
        Brute-force has time limit exceed.
        R: O(n)
        M: O(1)
        """
        left, right, best = 0, 1, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                best = max(best, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return best


if __name__ == "__main__":

    s = Solution()

    tests = (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    )

    for test in tests:
        exec("assert s.maxProfit(test[0]) == test[1]")

    print("Well done!")
