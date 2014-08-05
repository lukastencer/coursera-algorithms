from math import atan2
from insertionSort import insertionSort
from llstack import llstack

def getminY(points):
    
    minY = 0
    for i in range(0,len(points)):
        print i
        if points[i][1] < points[minY][1]:
            minY = i
    return minY

def topolar(origin, point):
    tempPoint = [0]*2
    
    tempPoint[0] = point[0] - origin[0]
    tempPoint[1] = point[1] - origin[1]
    
    return atan2(tempPoint[1],tempPoint[0])

def less180(x1,x2,x3):
    v1 = [x2[0]-x1[0],x2[1]-x1[1]]
    v2 = [x3[0]-x2[0],x3[1]-x2[1]]
    
    if ((v1[0]*v2[1]) - (v2[0]*v1[1])) > 0:
        return 1
    else:
        return 0

class grahamHull():
    
    sort = insertionSort()
    hull = llstack()
    
    def getHull(self,arr):
        
        polar = []
        polarSorted = []
        
        minY = getminY(arr)
        
        for point in arr:
            polar.append(topolar(arr[minY], point))
            
        idxarr = self.sort.sortIdx(polar)
        
        for idx in idxarr:
            polarSorted.append(arr[idx])
            
        self.hull.push(polarSorted[0])
        self.hull.push(polarSorted[1])
        
        for i in range(2,len(polarSorted)):
            top = self.hull.pop()
            if less180(self.hull.peek(), top, polarSorted[i]):
                self.hull.push(top)
                self.hull.push(polarSorted[i])
            else:
                while not less180(self.hull.peek(), top, polarSorted[i]):
                    top = self.hull.pop()
                self.hull.push(top)
                self.hull.push(polarSorted[i])
            
        return self.hull.toList()