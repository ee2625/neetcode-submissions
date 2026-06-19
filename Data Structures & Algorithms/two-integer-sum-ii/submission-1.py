class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        group = {}
        ans = []
        i = 1
        for x in range(len(numbers)):
            if target - numbers[x] in group:
                return [group[target - numbers[x]],i]
            else:
                group[numbers[x]] = i
                i += 1
        return ans