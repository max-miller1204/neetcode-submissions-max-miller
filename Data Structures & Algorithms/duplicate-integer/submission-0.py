class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = set()
        for num in nums:
            if num in valid:
                return True
            valid.add(num)
        return False