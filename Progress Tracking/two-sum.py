class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashM = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in HashM:
                return [HashM[diff],i]
            HashM[n] = i
        return  