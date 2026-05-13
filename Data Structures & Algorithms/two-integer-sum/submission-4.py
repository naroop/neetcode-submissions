class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i,n in enumerate(nums):
            lookup[n] = i

        for n in range(len(nums)):
            need = target - nums[n]
            x = lookup.get(need, -1)

            if x == n:
                continue

            if x != -1:
                return [n, x]

        return []