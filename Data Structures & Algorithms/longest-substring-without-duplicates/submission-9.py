class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = []
        best = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.append(s[i])
            best = max(best,i - left + 1)
        return best
