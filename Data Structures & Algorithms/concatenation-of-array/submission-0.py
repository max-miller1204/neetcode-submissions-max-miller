class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * (2 * n)

        for i in range(0, n):
            ans[i] = nums[i]

        for i in range(n, len(ans)):
            ans[i] = nums[i - n]

        return ans
