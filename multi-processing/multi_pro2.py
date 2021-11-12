import multiprocessing
import time

#시작시간
start_time = time.time()

#멀티쓰레드 사용 하는 경우 (20만 카운트)
#Pool 사용해서 함수 실행을 병렬
def count(name):
    for i in range(1,50001):
        print(name," : ",i)

num_list = ['p1', 'p2', 'p3', 'p4']

if __name__ == '__main__':
    #멀티 쓰레딩 Pool 사용
    pool = multiprocessing.Pool(processes=2) # 현재 시스템에서 사용 할 프로세스 개수
    pool.map(count, num_list)
    pool.close()
    pool.join()

print("--- %s seconds ---" % (time.time() - start_time))
