class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        for val in strs:
            key = ''.join(sorted(val))
            if key in seen:
                ans[seen[key]].append(val)
            else:
                ans.append([val])
                seen[key] = len(ans) - 1
        return ans