class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minimum = 0
        for log in logs: 
            if log == "../":
                if minimum>0:
                    minimum-=1
            elif log == "./":
                continue
            else:
                minimum+=1
        return minimum 