from mergesort import mergesort

a = [1, 5, 6, 88, 90, 2, 3, 56, 57, 100]

aux = [0] * 10

m = mergesort() 

print m.sort(a) == m.merge(a, aux, 0, 4, 9)

print a