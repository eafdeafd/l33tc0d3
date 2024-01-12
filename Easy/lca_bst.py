'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
1.4M
Submissions
2.2M
Acceptance Rate
63.9%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Solution 1. O(n) space, general Binary Tree search for LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q, False, False, None)[2]
    def lca(self, curr, p, q, pFound, qFound, ancestor):
        if not curr:
            return False, False, None
        if ancestor:
            return True, True, ancestor
        qFoundRight, pFoundRight, ancestorRight = self.lca(curr.right, p, q, pFound, qFound, ancestor)
        qFoundLeft, pFoundLeft, ancestorLeft = self.lca(curr.left, p, q, pFound, qFound, ancestor)
        if ancestorRight:
            return True, True, ancestorRight
        if ancestorLeft:
            return True, True, ancestorLeft
        qFound = True if curr == p or qFoundLeft or qFoundRight else False
        pFound = True if curr == q or pFoundLeft or pFoundRight else False
        if qFound and pFound:
            return True, True, curr
        return qFound, pFound, None

# Solution 2. O(1) space, BST 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (True):
            if p.val < root.val and q. val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
        return root
