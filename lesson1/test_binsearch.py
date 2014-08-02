from binsearch import binsearch

bs = binsearch()

array = [1, 3, 5, 17, 25, 31, 33, 45, 55, 56, 57, 87, 90, 99]

q = 1
print bs.search(array, q) == 0

q = 5
print bs.search(array, q) == 2 

q = 87
print bs.search(array, q) == 11 

q = 99
print bs.search(array, q) == 13 

q = 6
print bs.search(array, q) == -1 

q = 60
print bs.search(array, q) == -1