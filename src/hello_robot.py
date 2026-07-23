import numpy as np
import matplotlib.pyplot as plt

# 模擬超音波數據 (機器人靠近牆壁)
np.random.seed(100)
time = np.linspace(0, 10, 40)
true_dist = np.linspace(5.0, 0.5, 40)
raw_distance = true_dist + np.random.normal(0, 0.4, 40) # 帶有雜訊的測距值

# 2.距離平均  (Window Size = 3)
smooth_distance = np.zeros_like(raw_distance) # 建立一個同維度的空陣列

# 利用 NumPy 邊界切片算平均
for i in range(len(raw_distance)):
    if i < 2:
        smooth_distance[i] = raw_distance[i] 
    elif i >= len(raw_distance) - 2:
        smooth_distance[i] = raw_distance[i] 
    else:
        # 關鍵：取 [前後兩點加自己] 的平均
        smooth_distance[i] = np.mean(raw_distance[i-2 : i+3])

# 3. 視覺化對比：原始雜訊 vs 距離平滑數據
plt.figure(figsize=(10, 5))
plt.plot(time, raw_distance, label='Raw Distance (Noisy)', color='gray', alpha=0.5, linestyle='--')
plt.plot(time, smooth_distance, label='Filtered Distance (Smoothed)', color='blue', linewidth=2)
plt.axhline(y=1.0, color='red', linestyle=':', label='Safety Margin (1.0m)') 
unsafe_mask = smooth_distance < 1.0
plt.scatter(time[unsafe_mask], smooth_distance[unsafe_mask], label='Unsafe Points', color='red', alpha=1, s=50) # 標記低於安全距離的點

plt.title('Distance Filtering (5-Point Moving Average)')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.grid(True)
plt.legend()
plt.show()