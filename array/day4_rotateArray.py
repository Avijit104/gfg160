class Solution: 
    def rotateArr(self, arr, d):
        #Your code here
        a = d % len(arr)
        if a == len(arr):
            return arr
        else:
            res = arr[a:] + arr[:a]
            for i in range(len(res)):
                arr[i] = res[i]
                
        
        
            n = len(arr)
            
            
            #juggling algorithm for rotating an array 
            # we need to import math to fint out gcd for cycles

            # # Handle the case where d > size of array
            # d %= n

            # # Calculate the number of cycles in the rotation
            # cycles = math.gcd(n, d)

            # # Process each cycle
            # for i in range(cycles):
                
            #     # Start element of current cycle
            #     startEle = arr[i]
                
            #     # Start index of current cycle
            #     currIdx = i
                
            #     # Rotate elements till we reach the start of cycle
            #     while True:
            #         nextIdx = (currIdx + d) % n
                    
            #         if nextIdx == i:
            #             break
                    
            #         # Update the next index with the current element
            #         arr[currIdx] = arr[nextIdx]
            #         currIdx = nextIdx
                
            #     # Copy the start element of current cycle at the last
            #     # index of the cycle
            #     arr[currIdx] = startEle