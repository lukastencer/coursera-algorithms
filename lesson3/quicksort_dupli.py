from random import shuffle

def qsort(array):
    
    shuffle(array)
    __qsort(array, 0, len(array)-1)
    
def __qsort(array,low,high):
    
    if(high <= low): return
    lowp = low
    highp = high
    
    piv = array[low]
    i = low
    
    while (i <= highp):
        if array[i] < piv:
            array[lowp],array[i]=array[i],array[lowp]
            lowp +=1
            i += 1
        elif array[i] > piv:
            array[highp],array[i]=array[i],array[highp]
            highp -=1
        else:
            i+=1
            
    __qsort(array,low,lowp-1)
    __qsort(array,highp+1,high)
    
test = [5, 4, 3, 9, 8, 7, 11, 1, 67, 2]
print test

qsort(test)
print test