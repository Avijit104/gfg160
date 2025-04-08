#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        pvt = -1
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > arr[i-1]:
                pvt = i - 1
                break
        if pvt == -1 :
            arr.reverse()
            return
        for i in range(len(arr)-1, pvt, -1):
            if arr[i] >arr[pvt]:
                arr[i], arr[pvt] = arr[pvt], arr[i] 
                break
        left = pvt+1
        right = len(arr)-1
        while left<right :
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
