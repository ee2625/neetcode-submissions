class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        ans = []

        for value in strs:
            key = ''.join(sorted(value))

            if key in count:
                ans[count[key]].append(value)
            else:
                count[key] = len(ans)
                ans.append([value])

        return ans