class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        arr = []
        left = 0
        best = float('inf')
        for i in range(len(nums)):
            arr.append(nums[i])
            while sum(arr) >= target:
                best = min(best,len(arr))
                arr.remove(nums[left])
                left += 1
                
            
        
        if best == float('inf'):
            return 0
        else:
            return best
            