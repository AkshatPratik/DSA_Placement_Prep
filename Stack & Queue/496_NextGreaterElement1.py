class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = {}

        for num in nums2:
            while stack and num > stack[-1]:
                small = stack.pop()
                result[small] = num
            stack.append(num)
        
        answer = []
        for num in nums1:
            if num in result:
                answer.append(result[num])
            else:
                answer.append(-1)
        return answer