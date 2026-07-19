class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = []
        best = 0
        for val in s:
            while val in seen:
                seen.remove(s[left])
                left += 1
            seen.append(val)
            best = max(best,len(seen))
        return best