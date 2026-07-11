class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        left = 0
        best = 0
        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[left])
                left += 1
            ans.add(s[i])
            best = max(best,len(ans))
        return best
