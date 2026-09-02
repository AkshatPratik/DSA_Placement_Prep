class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        chars = set()
        longest = 0 

        for right in range(n):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longest = max(longest,right-left+1)
        return longest
