class insertionSort:
    
    def sort(self,arr):
        
        for i in range(0,len(arr)):
            
            for j in range(i,0,-1):
                if j-1 < 0:
                    break
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
            
        return arr
    
    def sortIdx(self,arr):
        
        idx = range(0,len(arr))
        
        for i in range(0,len(arr)):
            
            for j in range(i,0,-1):
                if j-1 < 0:
                    break
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    
                    idx[j], idx[j-1] = idx[j-1], idx[j]
                    
                else:
                    break
            
        return idx
 