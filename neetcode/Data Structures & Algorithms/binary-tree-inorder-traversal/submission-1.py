# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Used result to store traversal order.
        result = []

        # Used stack for iterative traversal.
        stack = []

        # Continued while nodes remained to process.
        while root or stack:

            # Moved to leftmost node.
            while root:
                stack.append(root)
                root = root.left

            # Retrieved next node to visit.
            root = stack.pop()

            # Added current node value.
            result.append(root.val)

            # Moved to right subtree.
            root = root.right

        # Returned inorder traversal.
        return result  