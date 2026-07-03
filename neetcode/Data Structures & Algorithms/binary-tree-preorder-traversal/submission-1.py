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

        # Used current to traverse tree.
        current = root

        # Traversed tree until all nodes were processed.
        while current:

            # Processed node if left child did not exist.
            if not current.left:

                # Added current node value.
                result.append(current.val)

                # Moved to right child.
                current = current.right

            else:

                # Used predecessor to find rightmost node.
                predecessor = current.left

                # Found inorder predecessor.
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # Created temporary thread.
                if not predecessor.right:

                    # Added current node value.
                    result.append(current.val)

                    predecessor.right = current

                    current = current.left

                # Removed temporary thread.
                else:

                    predecessor.right = None

                    current = current.right

        # Returned preorder traversal.
        return result