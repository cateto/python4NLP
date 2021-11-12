import time

#시작시간
start_time = time.time()

#멀티쓰레드 사용 하지 않은 경우 (20만 카운트)
def count(name):
    for i in range(1,50001):
        print(name," : ",i)

num_list = ['p1', 'p2', 'p3', 'p4']
for num in num_list:
    count(num)

print("--- %s seconds ---" % (time.time() - start_time))
