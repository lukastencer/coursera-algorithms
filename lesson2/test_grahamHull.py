from Tkinter import *
from Crypto.Random.random import randint
from grahamHull import grahamHull

hullMaker = grahamHull()
master = Tk()
resMax = 600
margin = 100

w = Canvas(master, width=resMax, height=resMax)
w.pack()

allPoints = []
hullPoints = []

for i in range(0,150):
    allPoints.append([randint(0+margin,resMax-margin),randint(0+margin,resMax-margin)])

#allPoints = [[100,100],[200,200],[150,160],[140,170],[110,220]]
print allPoints

hullPoints = hullMaker.getHull(allPoints)

#hullPoints = allPoints

print allPoints

for point in allPoints:
    w.create_oval(point[0],point[1],point[0]+5,point[1]+5,fill="red")
    
for i in range(0,len(hullPoints)):
    if i < len(hullPoints)-1:
        w.create_line(hullPoints[i][0],hullPoints[i][1],hullPoints[i+1][0],hullPoints[i+1][1])
    else:
        w.create_line(hullPoints[i][0],hullPoints[i][1],hullPoints[0][0],hullPoints[0][1])        

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#
# w.create_oval(50, 25, 150, 75, fill="blue")

mainloop()