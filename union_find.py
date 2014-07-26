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