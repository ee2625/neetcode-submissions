class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = []
        best = 0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[left])
                left += 1
            ans.append(s[i])
            best = max(best,i-left+1)
        return best