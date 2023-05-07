
# from multiprocessing import Process
from functools import partial
from multiprocessing import Pool, Process
from time import sleep, time
from numba import njit

start = time() * 1000
# @njit(cache = True)
def test1():
    allData = []
    for i in range(10000000):
        if i % 2 == 0:
            allData.append(i) 
        else:
            continue
    return len(allData)


# test11 = njit(test1)
# print(test11(), f"last for {(time() * 1000) - start}ms")

def run_compailed_func(time1,text):
    time1 = time()*1000
    print("ye")
    print(text,test1(),time()*1000-time1)




# run_compailed_func(time1,"compaidel time: ")
if __name__ == '__main__':
    time1 = time()*1000
    Pool(processes=4).map(partial(run_compailed_func,time1),["compaidel time: ", "compaidel time: ", "compaidel time: ", "compaidel time: "])
    # print((time() * 1000) - time1)
    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    print((time() * 1000) - time1)
    # sleep(5)
    # print("passingSleepTIme")
    # time11 = time()*1000
    # Process(target=run_compailed_func, args=[time11,"compaidel time: "]).start()
    # Process(target=run_compailed_func, args=[time11,"compaidel time: "]).start()

    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # Process(target=run_compailed_func, args=[time1,"compaidel time: "]).start()
    # run(time1,"compaidel time: ")
    # text = "compaidel time: "
    # Thread(target=run, args=[testC, time1,"compaidel time: "]).start()
    # Thread(target=run, args=[testC, time1,"compaidel time: "]).start()
    # Thread(target=run, args=[testC, time1,"compaidel time: "]).start()

    # run_compailed_func(time1,"compaidel time: ")
        
