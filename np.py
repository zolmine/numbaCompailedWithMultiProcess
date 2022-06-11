from numba import njit, set_num_threads

@njit(parallel=True)
def func():
    allData = []
    for i in range(10000000):
        if i % 2 == 0:
            allData.append(i) 
        else:
            continue
    return len(allData)

set_num_threads(2)
func()