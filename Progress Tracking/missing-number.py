class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        TotSum = (n*(n+1)) // 2
        MSum = sum(nums)
        return TotSum - MSum