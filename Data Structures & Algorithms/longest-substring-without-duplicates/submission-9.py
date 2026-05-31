class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        hash = defaultdict(int)
        hash[s[left]] = 1
        length = 0
        while left < right and right < len(s):
            if hash[s[right]] == 1:
                length = max(length, right - left)
                while s[left] != s[right]:
                    hash[s[left]] -= 1
                    left += 1
                left += 1
            else:
                length = max(length, right - left+1)
                hash[s[right]] += 1
            right += 1
        return length
            
