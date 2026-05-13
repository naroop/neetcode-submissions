class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(list)

        for n in nums:
            for i in range(len(nums)):
                if n not in freqs[i]:
                    freqs[i].append(n)
                    break
        
        for j in range(len(nums) - 1, -1, -1):
            if len(freqs[j]) == k:
                return freqs[j]