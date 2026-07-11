class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        for num in strs:
            key = ''.join(sorted(num))
            if key in seen:
                ans[seen[key]].append(num)
            else:
                seen[key] = len(ans)
                ans.append([num])
        return ans
