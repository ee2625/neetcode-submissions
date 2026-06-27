class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        s = sorted(s)
        t = sorted(t)

        for value in s:
            count1[value] = count1.get(value,0) + 1
        for value in t:
            count2[value] = count2.get(value,0) + 1
        return s == t