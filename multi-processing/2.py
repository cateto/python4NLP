import time
import multiprocessing

#시작 시간
start_time = time.time()

# without multi-thread
def count(name):
    sum = 0
    for i in range(1,50001):
        sum+= i

num_list = ['p1', 'p2', 'p3', 'p4']

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2) # process 2
    pool.map(count, num_list)
    pool.close()
    pool.join()
    
print(f'--- {time.time() - start_time } seconds')