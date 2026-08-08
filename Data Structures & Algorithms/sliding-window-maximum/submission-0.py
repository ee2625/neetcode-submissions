class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indices
        result = []

        for i in range(len(nums)):

            # Remove indices that are outside the window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove smaller values from the right
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Start recording answers once window reaches size k
            if i >= k - 1:
                result.append(nums[q[0]])

        return result