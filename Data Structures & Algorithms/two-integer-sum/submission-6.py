class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            c = target - nums[i]
            exist = complements.get(c, -1)
            if exist != -1:
                return [complements[c], i]
            complements[nums[i]] = i

        return []