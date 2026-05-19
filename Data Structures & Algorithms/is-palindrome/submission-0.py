class Solution:
    def isPalindrome(self, s: str) -> bool:
        sr = s.lower()
        sr = ''.join(char for char in sr if char.isalnum())
        return sr == sr[::-1]