import random
class CallStore:
    def __init__(self,size=50):
        self.switchCountries = [ "US", "China", "UK", "Germany", "Australia" ]
        self.NumPrefix = [ "0123", "1234", "2345", "3456","4567","5678", "6789","7890" ]
        self.callNos=[""]*size
        for i in range(size):
            prefixIdx=random.randint(0,len(self.NumPrefix)-1)
            prefix = self.NumPrefix[prefixIdx]
            self.callNos[i]="{} {:05d}".format(prefix,i)


if __name__=="__main__":
    callStore=CallStore()
    for i in range(50):
        print(callStore.callNos[i])

