#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        c = set(a)
        d = set(b)
        if c.issubset(d):
            print("true")
        else: 
            print("false")
    
    
    
    
