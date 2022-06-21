from sys import prefix
from traceback import print_tb
from datetime import datetime
import datetime
import random
from datetime import timedelta
class test:
    def __init__(self) -> None:
        self.gms=1
        self.ntt=3
        self.check=dict()
        self.check[0]=self.ntt

    def setData(self,key,value):
       print(self.check.get(0))
       self.adsd=222

        # print(self.key)
        # self.key=value
        # for i in ["ntt","gms"]:
            # if i == key:
            #     self.i

if __name__=="__main__":
    # t1=test()
    # print(t1.ntt)
    # t1.setData("ntt",12)
    # print(t1.ntt)
    # print(t1.adsd)
    # print("aaaaa".__eq__("aaaaa"))
    # print("aaaaa"=="aaaaa")
    # print(datetime.datetime.now())
    ptTime = datetime.datetime.now()
    # endTime=ptTime + timedelta(hours=2)
    # print(ptTime<endTime)
    # print(ptTime>endTime)
    # print(ptTime==endTime)
    # # print(random())
    # print(round(random.random(), 1))
    # print(ptTime)
    # s=datetime(str(ptTime)[11:])
    callTime = ptTime.strftime("%H:%M:%S.%f")
    print(callTime)

    # print(random.randint(0, 30))
    # for i in range(10):
    #     print(i)
    #     i=i+1