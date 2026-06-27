class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        group = {}
        for i in range(len(strs)):
            sort = ''.join(sorted(strs[i]))
            if sort in group:
                ans[group[sort]].append(strs[i])
            else:
                group[sort] = len(ans)
                ans.append([strs[i]])
        return ans