import numba
from time import time

# @numba.njit(cache = True)
def test1():
    allData = []
    for i in range(10000000):
        if i % 2 == 0:
            allData.append(i) 
        else:
            continue
    return len(allData)

def run_compailed_func(time1,text):
    time1 = time()*1000
    print(text,test1(),time()*1000-time1)

