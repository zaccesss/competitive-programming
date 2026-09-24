# definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # used result to store traversal order.
        result = []

        def dfs(node):

            # returned if node was null.
            if not node:
                return

            # traversed left subtree first.
            dfs(node.left)

            # added current node value.
            result.append(node.val)

            # traversed right subtree.
            dfs(node.right)

        # started DFS from root.
        dfs(root)

        # returned inorder traversal.
        return result  