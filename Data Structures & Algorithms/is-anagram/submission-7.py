class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for val in s:
            count1[val] = count1.get(val,0) + 1
        for val in t:
            count2[val] = count2.get(val,0) + 1
        return count1 == count2