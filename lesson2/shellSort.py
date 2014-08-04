class shellSort:
    
    def sort(self,arr):
        
        hval = []
        
        h=0
        while (h < len(arr)/3):
            hval.insert(0, 3*h+1)
            h += 1
        
        
        for h in hval:
            for i in range(h,len(arr)):
                
                for j in range(i,-1,-h):
                    if j-h < 0:
                        break
                    if arr[j] < arr[j-h]:
                        arr[j], arr[j-h] = arr[j-h], arr[j]
            
        return arr