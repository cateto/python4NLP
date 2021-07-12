import numpy as np
# x = np.array([1,2,3])
# print(x)

# 행렬의 계산

x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])
x + y
x * y
x / y
x / 2.0 # 브로드 캐스트 기능

A = np.array([[1,2],[3,4]])
print(A)
A.shape
A.dtype
B = np.array([[3,0],[0,6]])
A + B
A * B
A * 10 # 브로드 캐스트

# 브로드 캐스트 -> 스칼라값을 확대

A = np.array([1,2],[3,4])
B = np.array([10,20])
A * B

# 원소 접근

X = np.array([[51,55],[14,19],[0,4]])
print(X)
print(X.shape)
X[0]
X[0][1]

for row in X:
    
    print(row)