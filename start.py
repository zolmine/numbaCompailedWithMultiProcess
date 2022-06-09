
import numba
from multiprocessing import Process
from time import time


# @numba.njit(cache = True)

def test1():
    allData = []
    for i in range(10000000):
        if i % 2 == 0:
            allData.append(i) 
        else:
            continue
    return allData


startTime = time()*1000 
test1()
print("first time: ", time()*1000 - startTime)




if __name__ == '__main__':
    startTime = time()*1000 
    # test1()
    Process(target=test1).start()
    print("compaidel time taken: ", time()*1000 - startTime)

