class Solution:
    def reverseArray(self, arr):
        # code here
        # left = 0
        # right = len(arr) -1
        # while(left < right):
        #     temp = arr[left]
        #     arr[left] = arr[right]
        #     arr[right] = temp
        #     left += 1
        #     right -= 1
        n = len(arr)
        for i in range(n // 2):
            temp = arr[i]
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp
            