import numpy as np
import matplotlib.pyplot as plt

# 這是橫向發展的矩陣：每一列 (Row) 代表一顆馬達的所有時間數據
raw_data = np.array([
    [1.5, 3.2, 1.8, 1.2],  # Motor 1
    [1.2, 1.4, 4.5, 1.1],  # Motor 2
    [1.0, 1.1, 1.2, 1.3]   # Motor 3
])

matrix_current = raw_data.T

total_current = np.sum(matrix_current, axis=1)
print("Total current at each time step:", total_current)


#劃出各馬達和總和的電流隨時間圖

time = np.arange(4) # 時間點 0, 1, 2, 3

# 這時候 matrix_current 的行 (Column) 分別就是 Motor 1, 2, 3
for i in range(matrix_current.shape[1]):
    plt.plot(time, matrix_current[:, i], label=f'Motor {i+1}', marker='o')

# 把總電流也畫上去（長度同樣是 4，完美對齊！）
plt.plot(time, total_current, linestyle='--', label='Total Current', marker='s')
plt.title('Current Over Time')    
plt.xlabel('Time Step')
plt.ylabel('Current (A)')
plt.legend()    
plt.grid()
plt.show()