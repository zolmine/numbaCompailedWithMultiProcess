
# from threading import Thread

from functions import run_compailed_func
from runFunctions import *
from multiprocessing import Process
from time import time








if __name__ == '__main__':
    print("start")
    
    time1 = time()*1000
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()

    # run_compailed_func(time1,"compaidel time: ")
        
