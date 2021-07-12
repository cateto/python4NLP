import numpy as np
import matplotlib.pyplot as plt

#데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1간격으로 데이터 형성
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")

plt.xlabel("x축이다")
plt.ylabel("y축이다")
plt.title('sin & cos')
plt.legend() #범례 보이기
plt.show()

#### my 실습

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = (3 * x) + 5

plt.plot(x,y)
plt.show()

