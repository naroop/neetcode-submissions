class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for n in range(len(nums)):
            need = target - nums[n]

            if need in previous:
                return [previous[need], n]

            previous[nums[n]] = n

        return []