class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        arr = set()
        best = 0
        for i in range(len(s)):
            if s[i] not in arr:
                arr.add(s[i])
                best = max(best,len(arr))
            else:
                while s[i] in arr:
                    arr.remove(s[left])
                    left += 1
                arr.add(s[i])
        return best

            