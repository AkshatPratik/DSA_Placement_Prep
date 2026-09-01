class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        minimum = float('inf')

        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                length = right-left+1
                minimum = min(minimum,length)
                current_sum -= nums[left]
                left += 1
        
        if sum(nums) < target:
            return 0

        return minimum
