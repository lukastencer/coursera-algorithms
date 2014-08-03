class llstack:
    
    class node():
        
        next = None
        val = None
        
        def __init__(self,nextNode,val):
                    
            self.next = nextNode
            self.val = val
        
    head = None
    
    def push(self,inVal):
        
        if self.head == None:
            self.head = self.node(None,inVal)
        else:
            tempH = self.head
            self.head = self.node(tempH,inVal)
        
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