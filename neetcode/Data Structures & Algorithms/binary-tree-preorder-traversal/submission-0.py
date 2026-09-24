# definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # used result to store traversal order.
        result = []

        def dfs(node):

            # returned if node was null.
            if not node:
                return

            # added current node value first.
            result.append(node.val)

            # traversed left subtree.
            dfs(node.left)

            # traversed right subtree.
            dfs(node.right)

        # started DFS from root.
        dfs(root)

        # returned preorder traversal.
        return result