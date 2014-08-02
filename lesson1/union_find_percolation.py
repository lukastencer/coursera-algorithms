from union_find import UFindWeightPathComp
from random import randint

class Percolation:
    
    __UFstruct = None
    __GridSize =  None
    __GridDim = None
    __OpenRec = None
    
    def __init__(self,sizeN):
        
        self.__GridSize =  sizeN*sizeN
        self.__GridDim = sizeN
        
        self.__OpenRec = [False] * self.__GridSize
        
        self.__UFstruct = UFindWeightPathComp( self.__GridSize + 2 )
        for i in range(0,sizeN):
            self.__UFstruct.union(i, self.__GridSize)
            
        for i in range(self.__GridSize-1,self.__GridSize-1-sizeN,-1):
            self.__UFstruct.union(i,self.__GridSize + 1)
        
    def __getNeighb(self,idx):
        res = []
        
        if idx > self.__GridDim - 1:
            res.append(idx-self.__GridDim)

        if idx % self.__GridDim < self.__GridDim - 1:
            res.append(idx + 1)
            
        if idx < (self.__GridSize - 1) - self.__GridDim:
            res.append(idx + self.__GridDim)
            
        if idx % self.__GridDim > 0:
            res.append(idx - 1)       
            
        return res
    
    def show(self):
        print self.__OpenRec
        print self.__UFstruct.getRecords()
        
    def flip(self):
        self.step(randint(0,self.__GridSize - 1))
        
    def step(self,inIdx):
        print 'flip'
        # TODO, check which are open, maybe need to change data structure and record already open
        
        randIdx = inIdx
        toConnect = self.__getNeighb(randIdx)
        
        if not self.__OpenRec[randIdx]:
            self.__OpenRec[randIdx] = True
            for elem in toConnect:
                if self.__OpenRec[elem]:
                    self.__UFstruct.union(randIdx,elem)
                    
        print 'The structure percolates:', self.__UFstruct.find(self.__GridSize, self.__GridSize + 1)
        
        
        
        