# definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # returned empty list if tree was empty.
        if not root:
            return []

        # used result to store traversal order.
        result = []

        # used stack for traversal.
        stack = [root]

        # processed nodes while stack was not empty.
        while stack:

            # retrieved current node.
            node = stack.pop()

            # added node value.
            result.append(node.val)

            # added left child first.
            if node.left:
                stack.append(node.left)

            # added right child second.
            if node.right:
                stack.append(node.right)

        # reversed to obtain postorder traversal.
        return result[::-1]