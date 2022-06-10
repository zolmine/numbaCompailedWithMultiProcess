
# from threading import Thread
# from functions import run_compailed_func
# from runFunctions import *
import asyncio
from multiprocessing import Process
from time import time
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
if __name__ == '__main__':
    print("start")
    text = "compaidel time: "
    time1 = time()*1000
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()

    # run_compailed_func(time1,"compaidel time: ")
        
