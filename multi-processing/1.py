import time

#시작 시간
start_time = time.time()

# without multi-thread
def count():
    sum = 0
    for i in range(1,50001):
        sum+= i

num_list = ['p1', 'p2', 'p3', 'p4']
for num in num_list:
    count()
    
print(f'--- {time.time() - start_time } seconds')