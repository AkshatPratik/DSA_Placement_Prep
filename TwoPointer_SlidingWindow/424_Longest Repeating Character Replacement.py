class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0 
        right = 0
        answer = 0
        count = {}

        for right in range(n):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right-left+1) 
        return answer