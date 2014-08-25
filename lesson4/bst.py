class node:
    val = None
    left = None
    right = None
    
    def __init__(self,val):
        self.val = val
        
    def gotplacefor(self,val):
        
        if (val < self.val) and (self.left == None):
            return True
        if (val > self.val) and (self.right == None):
            return True
        
        return False
        
class bst:
    
    root = None
    
    def add(self,val):
        if self.root == None:
            self.root = node(val)
        else:
            temp = self.root
            
            while not temp.gotplacefor(val):
                if val < temp.val:
                    temp = temp.left
                else:
                    temp = temp.right
            
            if val < temp.val:
                temp.left = node(val)
            else:
                temp.right = node(val)
            
        
    def dfs(self):
        temp = []
        tovisit = []
        
        tovisit.append(self.root)        
        
        while len(tovisit) > 0:
            current = tovisit[0]
            del tovisit[0]
            
            
            if not current.right == None:
                tovisit.insert(0, current.right)
            if not current.left == None:
                tovisit.insert(0, current.left)

            
            temp.append(current.val)     
            
        return temp
        
        
    def bfs(self):
        temp = []
        tovisit = []
        
        tovisit.append(self.root)        
        
        while len(tovisit) > 0:
            current = tovisit[0]
            del tovisit[0]
            
            
            if not current.left == None:
                tovisit.append(current.left)
            if not current.right == None:
                tovisit.append(current.right)


            
            temp.append(current.val)     
            
        return temp
    
    
tree = bst()

tree.add(10)
tree.add(5)
tree.add(15)
tree.add(1)
tree.add(7)
tree.add(11)
        
        
print tree.dfs()

        
print tree.bfs()