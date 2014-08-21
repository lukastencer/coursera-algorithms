from random import shuffle

def partition(array, low, high):
    i = low+1
    j = high
    
    while True:        
        
        while (array[i] < array[low]):
            if(i == high):
                break
            i += 1
    
        if j < 0 or low < 0 or low > len(array)-1 or j > len(array)-1:
            print 'boom'
    
        while (array[j] > array[low]):
            if(j == low):
                break
            j -= 1
            
        if i >= j:
            break
        
        array[i],array[j] = array[j], array[i]  

    array[low],array[j] = array[j], array[low]  
    #print array
    return j

def qsort(array):
    
    shuffle(array)
    __qsort(array, 0, len(array)-1)
    
def __qsort(array,low,high):
    
    #print array
    
    if (high <= low):
        return
    
    j = partition(array, low, high)
    __qsort(array, low, j-1)
    __qsort(array, j+1, high)
    
    
test = [5, 4, 3, 9, 8, 7, 11, 1, 67, 2]
print test

qsort(test)
print test

