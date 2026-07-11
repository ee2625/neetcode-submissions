# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(a,low,high):
            if not a:
                return True
            if a.val <= low:
                return False
            if a.val >= high:
                return False
            return bst(a.right,a.val,high) and bst(a.left,low,a.val)        
        return bst(root,-float('inf'),float('inf'))
            