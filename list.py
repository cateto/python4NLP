# 반복문으로 출력하기
a = [1,2,3,4,5,6,7,8]
for temp in a:
    print(temp)

# # enumerate로는 인덱스와 밸류를 같이 꺼낼 수 있다.
for index, value in enumerate(a):
    print(index, value)

# # enumerate로 인덱스 1부터 출력하기
for index, value in enumerate(a, start=1):
    print(index, value)

# # 인덱스로 요소를 출력하기
for i in range(len(a)):
    print(a[i])

# # while문으로 리스트 출력하기
i = 0
while i < len(a):
    print(a[i])
    i+=1

# 가장 작은 수와 큰 수 구하기
a = [3, 5, 21, 54, 82]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

print(smallest)

largest = a[0]
for i in a:
    if i > largest:
        largest = i

print(largest)

# 가장 작은 수와 큰 수 구하기 (sort 활용)
b = [3, 5, 21, 54, 99]
b.sort()
b[0]

b.sort(reverse=True)
b[0]

# 가장 작은 수와 큰 수 구하기 (min/max 활용)
c = [3, 500, 210, 1010, 99]
min(c)
max(c)
