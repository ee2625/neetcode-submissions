class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for value in s:
            if value in count1:
                count1[value] += 1
            else:
                count1[value] = 1
        for value in t:
            if value in count2:
                count2[value] += 1
            else:
                count2[value] = 1
        return count1 == count2