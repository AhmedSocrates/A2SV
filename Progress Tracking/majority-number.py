class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashM = {}
        n=len(nums)

        for i in nums:
            hashM[i] = hashM.get(i,0) + 1
            if hashM[i] > n//2:
                return i
            