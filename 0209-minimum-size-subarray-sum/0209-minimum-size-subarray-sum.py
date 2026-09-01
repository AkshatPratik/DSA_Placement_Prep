class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minimum = float('inf')
        left = 0 
        total_sum = 0

        for right in range(n):
            total_sum += nums[right]
            while total_sum >= target:
                length = right - left + 1
                minimum = min(minimum,length)
                total_sum -= nums[left]
                left += 1
        if sum(nums) < target:
            return 0
        
        return minimum
