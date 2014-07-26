from union_find import UFind,UFindQUnion,UFindWeightPathComp

print '--------------test quick find---------------------'

UFTestObject = UFind(10)

UFTestObject.union(0, 1)
print UFTestObject.getRecords()
UFTestObject.union(2, 3)
print UFTestObject.getRecords()
UFTestObject.union(4, 5)
print UFTestObject.getRecords()
UFTestObject.union(6, 7)
print UFTestObject.getRecords()
UFTestObject.union(8, 9)
print UFTestObject.getRecords()
UFTestObject.union(1, 4)
print UFTestObject.getRecords()
UFTestObject.union(0, 8)
print UFTestObject.getRecords()
print UFTestObject.components() == 3

print '--------------test quick union---------------------'

UFTestObject = UFindQUnion(10)

UFTestObject.union(0, 1)
print UFTestObject.getRecords()
UFTestObject.union(2, 3)
print UFTestObject.getRecords()
UFTestObject.union(4, 5)
print UFTestObject.getRecords()
UFTestObject.union(6, 7)
print UFTestObject.getRecords()
UFTestObject.union(8, 9)
print UFTestObject.getRecords()
UFTestObject.union(1, 4)
print UFTestObject.getRecords()
UFTestObject.union(0, 8)
print UFTestObject.getRecords()
print UFTestObject.components() == 3

print '---------test quick union find weighted--------------'

UFTestObject = UFindWeightPathComp(10)

UFTestObject.union(0, 1)
print UFTestObject.getRecords()
UFTestObject.union(2, 3)
print UFTestObject.getRecords()
UFTestObject.union(4, 5)
print UFTestObject.getRecords()
UFTestObject.union(6, 7)
print UFTestObject.getRecords()
UFTestObject.union(8, 9)
print UFTestObject.getRecords()
UFTestObject.union(1, 4)
print UFTestObject.getRecords()
UFTestObject.union(0, 8)
print UFTestObject.getRecords()
print UFTestObject.components() == 3
print UFTestObject.find(0, 9) == True
print UFTestObject.find(0, 1) == True
print UFTestObject.find(0, 2) == False
print UFTestObject.find(2, 3) == True
print UFTestObject.find(2, 6) == False
print UFTestObject.find(0, 9) == True