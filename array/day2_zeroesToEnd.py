# we also can do it using spliting array in two parts one is nonZero another is zero but this don't work in gfg site because of the driver code

class Solution:
    def pushZerosToEnd(self,arr):
        cnt = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                temp = arr[i]
                arr[i] = arr[cnt]
                arr[cnt] = temp
                cnt += 1
            return arr