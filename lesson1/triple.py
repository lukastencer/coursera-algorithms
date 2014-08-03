from binsearch import binsearch
        

class triple:
    
    bs = binsearch()
    
    def find(self,inArray):
        
        res = set()
        inArray = sorted(inArray)
        
        for i in inArray:
            for j in inArray:
                diff = -(i+j)
                if not self.bs.search(inArray, diff) == -1:
                    if not diff in [i,j]:
                        res.add(tuple(sorted([i,j,diff])))
        return res