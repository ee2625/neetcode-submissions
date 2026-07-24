class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans= []
        seen = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in seen:
                ans[seen[key]].append(strs[i])
            
            else:
                seen[key] = len(ans)
                ans.append([strs[i]])
        return ans