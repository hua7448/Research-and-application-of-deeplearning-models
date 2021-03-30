# import numpy as np
# import matplotlib.pyplot as mp

# # np.meshgrid 使用

# grid_x, grid_y = np.meshgrid(np.linspace(1, 5, 5),
#                              np.linspace(1, 5, 6))

# print(grid_x)
# print(grid_y)

# # sigmoid函数
# x = np.linspace(-20, 20, 500)
# y = 1 / (1 + np.exp(-x))

# # 绘制函数
# mp.figure("Sigmoid", facecolor="lightgray")
# mp.title("Sigmoid", fontsize=16)
# mp.grid(linestyle="-.")
# mp.plot(x, y)
# mp.tight_layout()
# mp.show()
'''
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.01)
a=np.array(x)
y1=(math.e**(x)-math.e**(-x))/(math.e**(x)+math.e**(-x))
plt.xlim(-11,11)
ax = plt.gca()# get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.plot(x,y1,label='Tanh',linestyle="-", color="green")#label为标签
plt.legend(['Tanh'])
plt.savefig('Tanh.png', dpi=500) #指定分辨
'''


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
x = np.arange(-10, 10)
y = np.where(x<0,0,x)#满足条件(condition)，输出x，不满足输出y
plt.xlim(-11,11)
plt.ylim(-11,11)
ax = plt.gca()# get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')# 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))#指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))

plt.plot(x,y,label='ReLU',linestyle="-", color="y")#label为标签
plt.legend(['ReLU'])
plt.savefig('ReLU.png', dpi=500)#指定分辨
