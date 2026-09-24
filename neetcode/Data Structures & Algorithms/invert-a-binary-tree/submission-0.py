# definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            # returned empty tree
            return None

        # swapped children
        root.left, root.right = root.right, root.left

        # processed left subtree
        self.invertTree(root.left)

        # processed right subtree
        self.invertTree(root.right)

        # returned inverted tree
        return root