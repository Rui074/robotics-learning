import numpy as np
import matplotlib.pyplot as plt

# 機器人每一次移動的相對位移 (dx, dy)
dx = np.array([1.0,  1.5,  0.5, -1.0, -0.5])
dy = np.array([0.5,  1.0,  2.0,  1.5, -1.0])
x_path = np.cumsum(dx)  # 結果會是：[1.0, 2.5, 3.0, 2.0, 1.5]
y_path = np.cumsum(dy)  # 結果會是：[0.5, 1.5, 3.5, 5.0, 4.0]
path_matrix = np.column_stack((x_path, y_path))  # 將 x_path 與 y_path 組合成一個二維矩陣
print("機器人的移動路徑矩陣:" , path_matrix)

# 繪製機器人的移動路徑
plt.figure(figsize=(8, 6))
plt.plot(x_path, y_path, marker='o', linestyle='-', color='b')
plt.title('Robot Movement Path')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.scatter(0.0, 0.0, color='green', label='Start Position')  # 標記起始位置
plt.scatter(x_path[-1], y_path[-1], color='red', label='End Position')  # 標記終點位置
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()