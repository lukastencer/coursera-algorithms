from Crypto.Random.random import randint
class knuthShuffle:
    def shuffle(self,arr):
        
        for i in range(0,len(arr)):
            idx = randint(0,i)
            arr[i], arr[idx] = arr[idx], arr[i]
            
        return arr