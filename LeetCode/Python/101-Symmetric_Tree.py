from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_equal(L, R):
            if not L and not R:
                return True

            # Important: at first look for None nodes and after for values
            if L and R and L.val == R.val:
                # We move first along the ribs to maximum depth (DFS Preorder) on both sides.
                # Turn right after reaching the bottom.
                return is_equal(L.left, R.right) and is_equal(L.right, R.left)
            return False

        return is_equal(root, root)


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

    assert s.isSymmetric(node_1) == True

    print("well done!")


