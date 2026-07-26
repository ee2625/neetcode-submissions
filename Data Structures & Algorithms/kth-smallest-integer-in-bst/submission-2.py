class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right