class llqueue:
    
    class node():
        
        next = None
        val = None
        
        def __init__(self,nextNode,val):
                    
            self.next = nextNode
            self.val = val
        
    head = None
    tail = None
    iterIdx = None
    
    def __iter__(self):
        self.iterIdx=self.head
        return self
    
    def next(self):
        
        if self.iterIdx == None:
            raise StopIteration
        data = self.iterIdx.val
        self.iterIdx = self.iterIdx.next
        return data

    
    def push(self,inVal):
        
        if self.head == None:
            self.head = self.node(None,inVal)
            self.tail = self.head
            
        else:
            tempT = self.tail
            self.tail = self.node(None,inVal)
            tempT.next=self.tail
        
    def pop(self):
        item = self.head.val;
        self.head = self.head.next;
        return item
    
    def show(self):
        tempP = self.head
        print '-------'
        
        while not tempP == None:
            print tempP.val
            tempP = tempP.next
    
    def parse(self,inString):
        
        parts = inString.split()
        
        for part in parts:
            if part == '-':
                self.pop()
            else:
                self.push(part)