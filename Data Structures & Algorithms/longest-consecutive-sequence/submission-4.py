class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_counts = defaultdict(int)

        for n in nums:
            num_counts[n] += 1

        longest = 0

        for n in nums:
            is_start_of_sequence = True if num_counts[n - 1] == 0 else False
            if is_start_of_sequence:
                seq = 0
                i = 0
                while True:
                    if num_counts[n + i] != 0:
                        seq += 1
                        i += 1
                    else:
                        break
                if seq > longest:
                    longest = seq


        return longest
