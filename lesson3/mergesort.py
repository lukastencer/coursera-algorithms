class mergesort:
    
    def merge(self,array,tempArray,low,mid,high):
        
        for i in range(low,high+1):
            tempArray[i] = array[i]
            
        i = low
        j = mid + 1 
        
        for k in range(low,high+1):
            
            if j > high:
                array[k] = array[i]
                i += 1                                
            elif i > mid:
                array[k] = array[j]
                j += 1
            
            elif tempArray[i] <= tempArray[j]:
                array[k] = tempArray[i]
                i += 1
            elif tempArray[j] < tempArray[i]:
                array[k] = tempArray[j]
                j += 1
                
    def __sort(self,array,tempArray,low,high):
        
        if high <= low: return
        mid = int(low + round((high - low) / 2))
        
        self.__sort(array, tempArray, low, mid)
        self.__sort(array, tempArray, mid + 1 , high)
        self.merge(array, tempArray, low, mid, high)
        
    def sort(self,array):
        
        tempArray = [0] * len(array)
        self.__sort(array, tempArray, 0, len(array)-1)

                
                
a = [1, 5, 6, 88, 90, 2, 3, 56, 57, 100]

aux = [0] * 10

m = mergesort()

#m.merge(a, aux, 0, 4, 9)
m.sort(a)

print a



