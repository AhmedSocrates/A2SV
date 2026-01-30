class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1000):
            i = i+1
            if (i%n == 0 and i%2 == 0):
                return i