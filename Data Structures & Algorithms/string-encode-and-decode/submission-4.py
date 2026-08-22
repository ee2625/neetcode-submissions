class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs)):
            length = len(strs[i])
            result += str(length) + '#' + strs[i]
        return result
    def decode(self, s: str) -> List[str]:
        left = 0
        ans = []
        i = 0 
        while i < len(s):
            if s[i] == '#':
                length = int(s[left:i])
                ans.append(s[i+1:i+1+length])
                left = i + 1 + length
                i = left
            else: 
                i += 1
        return ans
                
