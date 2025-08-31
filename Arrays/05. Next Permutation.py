class Solution:
    def nextPermutation(self, arr):
        # code here
        m1 = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                m1 = i
                break
    
    
        if m1 == -1:
            arr.reverse()
            
        else:
            m2 = 0
            for j in range(len(arr)-1, m1, -1):
                if arr[j] > arr [m1]:
                    m2 = j
                    break
            arr[m1], arr[m2] = arr[m2], arr[m1]
            arr[m1+1 : ]  = (arr[m1+1 : ])[ : : -1]
            
        
