class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = []
        best = 0
        for i in range(len(s)):
            if s[i] in ans:
                best = max(best,i-left)
                while s[i] in ans:
                    ans.remove(s[left])
                    left += 1
                ans.append(s[i])
            else:
                ans.append(s[i])
                best = max(best,i-left+1)
        if best > 0:
            return best
        else:
            return len(ans)