import numpy as np
import matplotlib.pyplot as plt

# 遙測數據
time = np.arange(7)
left_vel = np.array([2.0, 3.0, 3.0, -1.5, -2.0, 1.0, 0.0])
right_vel = np.array([2.0, 1.0, 3.0, -1.5,  2.0, 1.0, 0.0])
# 2. 計算平均速度 ((左輪速 + 右輪速)/2
center_vel = (left_vel + right_vel) / 2

# 3. 開啟畫布並設定大小
plt.figure(figsize=(8, 6))

# ======== 第一張圖：左右輪速原始數據 ========
plt.subplot(2, 1, 1) # 參數意義：2列, 1行, 第1張圖 (上半部)
plt.plot(time, left_vel, label='Left Wheel', marker='o', color='blue')
plt.plot(time, right_vel, label='Right Wheel', marker='o', color='green')
plt.ylabel('Speed (m/s)')
plt.title('Chassis Telemetry: Wheel Speeds and center_vel')
plt.grid(True)
plt.legend()

# ======== 第二張圖：平均速度 ========
plt.subplot(2, 1, 2) # 參數意義：2列, 1行, 第2張圖 (下半部)
plt.plot(time, center_vel, label='Average Speed', marker='s', color='purple')

# 畫一條 Y=0 的紅色虛線，代表「完美直行」的基準線
plt.axhline(0, color='red', linestyle='--', label='stop')
#(中心速度小於0)
plt.scatter(time[center_vel < 0], center_vel[center_vel < 0], color='red', marker='x', s=100)
plt.ylabel('center_vel (m/s)')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()

# 自動調整排版，避免上下兩張圖的字疊在一起
plt.tight_layout() 
plt.show()
