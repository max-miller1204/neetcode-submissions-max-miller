class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash set approach
        seq = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in seq:
                length = 1
                while (num + length) in seq:
                    length += 1
                longest = max(length, longest)
        return longest