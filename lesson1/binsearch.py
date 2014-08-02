from math import ceil

class binsearch:
    
    def search(self,inArray,elem):
        
        midIdx = int(ceil((len(inArray)-1)/2))
        #print int(midIdx)
        
        if (len(inArray) == 1) and (not inArray[0] == elem):
            return -1 
        
        if inArray[midIdx] == elem:
            return midIdx
        else:
            if inArray[midIdx] > elem:
                return self.search(inArray[0:midIdx],elem)
            if inArray[midIdx] < elem:
                res = self.search(inArray[midIdx+1:], elem)
                return -1 if res == -1 else midIdx + 1 + res 