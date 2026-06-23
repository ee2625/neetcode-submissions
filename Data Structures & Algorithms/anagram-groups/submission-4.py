class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        ans = []
        for value in strs:
            key = ''.join(sorted(value))
            if key in group:
                ans[group[key]].append(value)
            else:
                group[key] = len(ans)
                ans.append([value])
        return ans