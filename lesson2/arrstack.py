class arrstack:
    
    arr = [None]*2
    N = 0
    
    def push(self,inVal):
        arrLen = len(self.arr)
        
        if self.N == arrLen-1:
            newarr = [None]*((arrLen-1)*2)
            newarr[0:arrLen-1] = self.arr
            self.arr = newarr
        
        self.arr[self.N] = inVal
        self.N += 1
        
    def pop(self):
        
        arrLen = len(self.arr)
        
        if self.N == int((arrLen-1)/4):
            newarr = [None]*int((arrLen-1)/2)
            newarr = self.arr[0:int((arrLen-1)/2)]
            self.arr = newarr
        
        res = self.arr[self.N]
        self.arr[self.N] = None
        self.N -= 1
        return res
    
    def show(self):
        print '-------'
        
        for i in self.arr:
            print i
    
    def parse(self,inString):
        
        parts = inString.split()
        
        for part in parts:
            if part == '-':
                self.pop()
            else:
                self.push(part)