class UFind():
    
    __records = [] 
    
    def __init__(self,numElements):
        
        self.__records = [0]*numElements
        for i in range(0,numElements):
            self.__records[i]=i
        
    def find(self,elem1,elem2):
        return self.__records[elem1] == self.__records[elem2]
    
    def union(self,elem1,elem2):
        id1 = self.__records[elem1]
        id2 = self.__records[elem2]
        
        if not id1 == id2:                    
            for idx,elem in enumerate(self.__records):
                if (elem == id1) or (elem == id2):
                    self.__records[idx] = id1
        
    def components(self):
        return len(set(self.__records))
    
    def getRecords(self):
        return self.__records
    
class UFindQUnion():
    
    __records = [] 
    
    def __init__(self,numElements):
        
        self.__records = [0]*numElements
        for i in range(0,numElements):
            self.__records[i]=i
    
    def root(self,elemIdx):
        while(self.__records[elemIdx] != elemIdx):
            elemIdx = self.__records[elemIdx]
        
        return elemIdx
        
    def find(self,elem1,elem2):
        return self.root(elem1) == self.root(elem2)
    
    def union(self,elem1,elem2):
        r1 = self.root(elem1)
        r2 = self.root(elem2)
        
        self.__records[r1] = r2
        
    def components(self):
        uniqRoots = set()
        
        for i in range(0,len(self.__records)):
            uniqRoots.add(self.root(i))
            
        return len(uniqRoots)
    
    def getRecords(self):
        return self.__records
    
class UFindWeightPathComp():
    
    __records = [] 
    __treeSizes = []
    
    def __init__(self,numElements):
        
        self.__records = [0]*numElements
        self.__treeSizes = [1]*numElements
        
        for i in range(0,numElements):
            self.__records[i]=i
    
    def root(self,elemIdx):
        while(self.__records[elemIdx] != elemIdx):
            self.__records[elemIdx] = self.__records[self.__records[elemIdx]] 
            elemIdx = self.__records[elemIdx]
        
        return elemIdx
        
    def find(self,elem1,elem2):
        return self.root(elem1) == self.root(elem2)
    
    def union(self,elem1,elem2):
        r1 = self.root(elem1)
        r2 = self.root(elem2)
        
        if self.__treeSizes[r1] < self.__treeSizes[r2]:
            self.__records[r1] = r2
            self.__treeSizes[r2] += self.__treeSizes[r1]
        else:
            self.__records[r2] = r1
            self.__treeSizes[r1] += self.__treeSizes[r2]

        
    def components(self):
        uniqRoots = set()
        
        for i in range(0,len(self.__records)):
            uniqRoots.add(self.root(i))
            
        return len(uniqRoots)
    
    def getRecords(self):
        return self.__records