import numpy as np
import matplotlib.pyplot as plt

# 1. 模擬時間軸與左右輪速數據 (單位: m/s)
time = np.arange(8)
speed_left = np.array([1.0, 1.0, 3.0, 3.0, 1.0, -1.0, 1.0, 1.0])  
speed_right = np.array([1.0, 1.0, 0.5, -1.0, 1.0,  3.0, 1.0, 1.0]) 

# 2. 計算轉向差速 (左輪速 - 右輪速)
# NumPy 陣列可以直接相減，這會算出每一個時間點的速度差！
speed_diff = speed_left - speed_right

# 3. 開啟畫布並設定大小
plt.figure(figsize=(8, 6))

# ======== 第一張圖：左右輪速原始數據 ========
plt.subplot(2, 1, 1) # 參數意義：2列, 1行, 第1張圖 (上半部)
plt.plot(time, speed_left, label='Left Wheel', marker='o', color='blue')
plt.plot(time, speed_right, label='Right Wheel', marker='o', color='green')
plt.ylabel('Speed (m/s)')
plt.title('Chassis Telemetry: Wheel Speeds & Turning Differential')
plt.grid(True)
plt.legend()

# ======== 第二張圖：轉向差速 (Yaw Rate) ========
plt.subplot(2, 1, 2) # 參數意義：2列, 1行, 第2張圖 (下半部)
plt.plot(time, speed_diff, label='Speed Diff (Left - Right)', marker='s', color='purple')

# 畫一條 Y=0 的紅色虛線，代表「完美直行」的基準線
plt.axhline(0, color='red', linestyle='--', label='Zero Turn (Straight)')

plt.ylabel('Delta Speed (m/s)')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()

# 自動調整排版，避免上下兩張圖的字疊在一起
plt.tight_layout() 
plt.show()
