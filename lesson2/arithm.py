from llstack import llstack
from arrstack import arrstack

class arithm:
    
    valstack = llstack()
    opstack = arrstack()
    
    def eval(self,inStr):
    
        strList = inStr.split()
        
        for elem in strList:
            if elem == '(':
                continue
            elif elem == ')':
                val1 = self.valstack.pop()
                val2 = self.valstack.pop()
                op = self.opstack.pop()
                
                if op == '+':
                    self.valstack.push(val1 + val2)
                elif op == '-':
                    self.valstack.push(val1 - val2)
                elif op == '*':
                    self.valstack.push(val1 * val2)
                elif op == '/':
                    self.valstack.push(val1 / val2)
                else:
                    pass
                    
                
            elif elem in ['+','-','*','/']:
                self.opstack.push(elem)
            else:
                self.valstack.push(int(elem))
                
        return self.valstack.pop()