class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for x in s:
            if x in count1:
                count1[x] = count1.get(x,0) + 1
            else:
                count1[x] = 1
        
        for x in t:
            if x in count2:
                count2[x] = count2.get(x,0) + 1
            else:
                count2[x] = 1
        return count1 == count2
        