from knuthShuffle import knuthShuffle

arr = []
for i in range(0,100):
    arr.append(i)

shufler = knuthShuffle()

print shufler.shuffle(arr)
