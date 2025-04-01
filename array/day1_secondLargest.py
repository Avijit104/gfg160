#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max = -1
        secMax = -1
        for i in arr:
            if i > max:
                secMax = max
                max = i
            elif i > secMax and i < max:
                secMax = i
        return secMax
            