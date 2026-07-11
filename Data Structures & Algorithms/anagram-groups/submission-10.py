class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        for val in strs:
            key = ''.join(sorted(val))
            if key in seen:
                ans[seen[key]].append(val)
            else:
                seen[key] = len(ans)
                ans.append([val])
        return ans