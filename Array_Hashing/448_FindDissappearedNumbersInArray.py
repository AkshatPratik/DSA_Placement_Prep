class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        answer = []

        for i in range(1,n+1):
            if i not in nums_set:
                answer.append(i)
        return answer
