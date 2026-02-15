class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashM = {}
        res = set()
        for i in range(len(nums)):
            hashM[nums[i]] = hashM.get(nums[i],0) + 1
            if hashM[nums[i]]==2: 
                res.add(nums[i])
        
        return list(res)