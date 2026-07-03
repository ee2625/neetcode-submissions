# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(a,low,high):
            if not a:
                return True
            if a.val <= low:
                return False
            if a.val >= high:
                return False
            return bfs(a.left, low, a.val) and bfs(a.right, a.val, high)
        return bfs(root.right,root.val,float('inf')) and bfs(root.left,-float('inf'),root.val)