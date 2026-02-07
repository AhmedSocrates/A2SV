class Solution:    
    def findUnion(self, a, b):
        # code here
        setA = set(a)
        setB = set(b)
        new_set= set(setA|setB)
        return new_set