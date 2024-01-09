# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # At every layer, swap the left and rightchilds
        curr = root
        self.swap(curr)
        return root

    def swap(self, curr: Optional[TreeNode]):
        if curr:
            curr.left, curr.right = curr.right, curr.left
            self.swap(curr.left)
            self.swap(curr.right)
