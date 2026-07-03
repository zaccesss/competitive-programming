# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Returned empty list if tree was empty.
        if not root:
            return []

        # Used result to store traversal order.
        result = []

        # Used stack for traversal.
        stack = [root]

        # Processed nodes while stack was not empty.
        while stack:

            # Retrieved current node.
            node = stack.pop()

            # Added node value.
            result.append(node.val)

            # Added left child first.
            if node.left:
                stack.append(node.left)

            # Added right child second.
            if node.right:
                stack.append(node.right)

        # Reversed to obtain postorder traversal.
        return result[::-1]