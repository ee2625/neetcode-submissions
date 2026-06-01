class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for value in s:
            if value.isalnum():
                cleaned += value.lower()
        reverse = ''
        for value in cleaned:
            reverse = value + reverse
        if reverse == cleaned:
            return True
        else:
            return False