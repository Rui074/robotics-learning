import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 固定隨機種子
np.random.seed(2026)

# ---- 1. 電流數據 (包含雜訊) ----
time = np.linspace(0, 10, 30)
raw_current = 2.0 + 1.2 * np.sin(time) + np.random.normal(0, 0.3, 30)
smooth_current = np.zeros_like(raw_current)
for i in range(len(raw_current)):
    if i == 0:
        smooth_current[i] = raw_current[i]
    elif i == len(raw_current) - 1:
        smooth_current[i] = raw_current[i]
    else:
        # 關鍵：取 [前後加自己] 的平均
        smooth_current[i] = np.mean(raw_current[i-1 : i+2])


plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(time, raw_current, label='Raw Current (Noisy)', color='gray', alpha=0.5, linestyle='--')
plt.plot(time, smooth_current, label='Filtered Current (Smoothed)', color='blue', linewidth=2)
plt.axhline(y=3.0, color='red', linestyle=':', label='Nominal Current (3.0A)') 
unsafe_mask = smooth_current > 3.0
plt.scatter(time[unsafe_mask], smooth_current[unsafe_mask], label='Unsafe Points', color='red', alpha=1, s=50)
plt.title('Current Filtering (3-Point Moving Average)')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.grid(True)
plt.legend()


# ---- 2. 2D 移動數據 (相對位移 dx, dy) ----
dx = np.array([0, 0.5, 0.8, 1.0, 0.5, 0.0, -0.5, -0.8, -0.5, 0.0, 0.5, 1.0])
dy = np.array([0, 0.2, 0.5, 0.8, 1.0, 1.2,  1.0,  0.5,  0.0, 0.5, 0.8, 1.0])

x = np.cumsum(dx)
y = np.cumsum(dy)


plt.subplot(2, 1, 2)
plt.plot(x, y, label='Path ', color='gray', alpha=1)
plt.scatter(0, 0, label='start', color='green', alpha=1, s=50) 
plt.scatter(x[-1], y[-1], label='end', color='red', alpha=1, s=50)

plt.title('Path Planning (2D Movement)')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()