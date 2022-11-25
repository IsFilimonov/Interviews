from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        self.res = 0

        while queue:
            root, nums = queue.pop(0)

            if not root.left and not root.right:
                self.res = max(self.res, nums)

            if root.left:
                queue.append((root.left, nums + 1))

            if root.right:
                queue.append((root.right, nums + 1))

        return self.res


if __name__ == "__main__":
    s = Solution()

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(2)
    node_4 = TreeNode(3)
    node_5 = TreeNode(3)
    node_6 = TreeNode(4)
    node_7 = TreeNode(4)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_6
    node_3.right = node_5
    node_3.left = node_7

    assert s.maxDepth(node_1) == 3

    print("well done!")
