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

        # used current to traverse tree.
        current = root

        # traversed tree until all nodes were processed.
        while current:

            # processed node if left child did not exist.
            if not current.left:

                # added current node value.
                result.append(current.val)

                # moved to right child.
                current = current.right

            else:

                # used predecessor to find rightmost node.
                predecessor = current.left

                # found inorder predecessor.
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # created temporary thread.
                if not predecessor.right:

                    # added current node value.
                    result.append(current.val)

                    predecessor.right = current

                    current = current.left

                # removed temporary thread.
                else:

                    predecessor.right = None

                    current = current.right

        # returned preorder traversal.
        return result