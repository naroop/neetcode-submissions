class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqs = defaultdict(list)

        for n in nums:
            counts[n] += 1

        for n, count in counts.items():
            freqs[count].append(n)

        ans = []
        for i in range(len(nums), 0, -1):
            if len(freqs[i]) > 0:
                ans += freqs[i]

                if len(ans) == k:
                    return ans
