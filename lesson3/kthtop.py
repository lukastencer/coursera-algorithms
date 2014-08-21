from quicksort import partition
from random import shuffle

def kthtop(array,k):
    
    shuffle(array)
    
    low = 0
    high = len(array) - 1
    
    while(high > low):
        j = partition(array, low, high)
        if j < k: low = j + 1
        elif j > k: high = j - 1
        else: return array[k]
        
    return array[k]

test = [5, 4, 3, 9, 8, 7, 11, 1, 67, 2]
print test

print kthtop(test, 8)