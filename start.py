
# from threading import Thread
from functions import run_compailed_func
from runFunctions import *
from multiprocessing import Process

if __name__ == '__main__':
    print("start")
    text = "compaidel time: "
    time1 = time()*1000
    Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Thread(target=run_compailed_func, args=[time1,text]).start()

    # run_compailed_func(time1,"compaidel time: ")
        
