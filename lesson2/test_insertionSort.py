from insertionSort import insertionSort

testArr = [5, -7, 8, 99, -7, 19, 8, 22, 999, -70, 0]

insSort = insertionSort()
print insSort.sort(testArr)
print insSort.sort(testArr) == [-70, -7, -7, 0, 5, 8, 8, 19, 22, 99, 999]