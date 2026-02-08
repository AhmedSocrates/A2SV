class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        hashM = {}
        n = len(nums)
        for i in nums:
            hashM[i] = hashM.get(i,0) + 1
            if hashM[i] > n//3 and i not in result:
                result.append(i)
        return result