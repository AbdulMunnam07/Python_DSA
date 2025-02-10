# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None  # Base case: If empty, return None

        # Step 1: The last element in postorder is the root
        root_val = postorder.pop()  # Remove the last element from postorder
        root = TreeNode(root_val)   # Create the root node

        # Step 2: Find the root in inorder to split left and right subtrees
        inorder_index = inorder.index(root_val)

        # Step 3: Recursively construct right subtree first, then left subtree
        root.right = self.buildTree(inorder[inorder_index + 1 :], postorder)  # Right    subtree
        root.left = self.buildTree(inorder[: inorder_index], postorder)  # Left subtree

        return root
        