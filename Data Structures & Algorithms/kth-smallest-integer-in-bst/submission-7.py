class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            num = stack.pop()
            k -= 1
            if k == 0:
                return num.val
            
            current= num.right