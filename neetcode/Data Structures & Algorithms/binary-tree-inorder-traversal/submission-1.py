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

        # used stack for iterative traversal.
        stack = []

        # continued while nodes remained to process.
        while root or stack:

            # moved to leftmost node.
            while root:
                stack.append(root)
                root = root.left

            # retrieved next node to visit.
            root = stack.pop()

            # added current node value.
            result.append(root.val)

            # moved to right subtree.
            root = root.right

        # returned inorder traversal.
        return result  