class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        for x in s:
            count1[x] = count1.get(x,0) + 1
        for x in t:
            count2[x] = count2.get(x,0) + 1
        return count1 == count2