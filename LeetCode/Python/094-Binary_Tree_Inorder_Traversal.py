from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive + list comprehension
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive + outer Array
        T: O(n) because recursive T(n) = 2 * T(n/2) + 1
        S: worst O(n), average O(logn)
        """
        def helper(root: Optional[TreeNode], A: List):
            if root != None:
                helper(root.left, A)
                A.append(root.val)
                helper(root.right, A)

        A = []

        helper(root, A)

        return A

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        """
        Stack
        T: O(n)
        S: O(n)
        """
        A = []
        stack = []
        current = root

        while current != None or len(stack) > 0:
            while current != None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            A.append(current.val)
            current = current.right

        return A

    def inorderTraversal_Moris(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris Traversal: without recursive and stack
        T: O(n)
        S: O(1)
        """
        return ...


if __name__ == "__main__":

    print("Cant test simle!")
