# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Used result to store traversal order.
        result = []

        def dfs(node):

            # Returned if node was null.
            if not node:
                return

            # Added current node value first.
            result.append(node.val)

            # Traversed left subtree.
            dfs(node.left)

            # Traversed right subtree.
            dfs(node.right)

        # Started DFS from root.
        dfs(root)

        # Returned preorder traversal.
        return result