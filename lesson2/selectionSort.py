class selectionSort:
    
    def sort(self,arr):
        
        for i in range(0,len(arr)):
            minPosition = i
            for j in range(i,len(arr)):
                if arr[j] < arr[minPosition]:
                    minPosition = j
                    
            arr[i], arr[minPosition] = arr[minPosition], arr[i]
            
        return arr