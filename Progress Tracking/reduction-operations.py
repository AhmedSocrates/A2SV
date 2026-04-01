class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums.sort(reverse=True)

        uniq = []
        for x in nums:
            if not uniq or uniq[-1] != x:
                uniq.append(x)
        ops = 0
        prefix = 0

        for i in range(1,len(uniq)):
            prefix +=freq[uniq[i-1]]
            ops += prefix
        return ops