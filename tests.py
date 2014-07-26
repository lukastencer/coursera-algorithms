from union_find import UFind

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