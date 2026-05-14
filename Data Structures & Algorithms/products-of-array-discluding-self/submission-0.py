class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        
        postfix = [0] * len(nums)
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]

        for i in range(len(nums)):
            if i == 0:
                answer[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                answer[i] = prefix[i - 1]
            else:
                answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer
