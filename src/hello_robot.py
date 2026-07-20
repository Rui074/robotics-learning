import numpy as np
import matplotlib.pyplot as plt

# 三顆馬達在時間點 0, 1, 2, 3 的電流
m1 = np.array([1.5, 3.2, 1.8, 1.2])
m2 = np.array([1.2, 1.4, 4.5, 1.1])
m3 = np.array([1.0, 1.1, 1.2, 1.3])

matrix_current=np.column_stack((m1, m2, m3))

clipped_current = np.clip(matrix_current, 0.0, 3.0)

# 繪製三顆馬達的電流圖
time = np.arange(4)  # 時間點 0, 1, 2, 3
plt.plot(time, clipped_current[:, 0], label='Motor 1')
plt.plot(time, clipped_current[:, 1], label='Motor 2')
plt.plot(time, clipped_current[:, 2], label='Motor 3')
plt.xlabel('Time')
plt.ylabel('Current')
plt.title('Motor Currents Over Time')
plt.legend()

plt.show()