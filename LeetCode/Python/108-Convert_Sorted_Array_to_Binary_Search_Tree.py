from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Every step find middle and give recursive only indexes.
        R: O(n)
        S: O(n)
        """
        def build(left, right):
            while left < right:
                return

            middle = (left + right) // 2
            node = TreeNode(nums[middle])

            node.left = build(left, middle-1)
            node.right = build(middle+1, right)

            return node
        
        return build(0, len(nums)+1)




    def sortedArrayToBST_array(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Every step slice middle and return array slice.
        R: O(nlgn)
        S: O(n)
        """
        if not nums:
            return None

        middle = len(nums) // 2

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root


if __name__ == "__main__":
    s = Solution()

    print("well done!")

