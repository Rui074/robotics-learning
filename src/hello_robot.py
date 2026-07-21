import numpy as np
import matplotlib.pyplot as plt

# 數據：時間與電流
time = np.arange(6)
current = np.array([1.2, 2.8, 3.5, 1.8, 4.1, 2.0])

# 1. 找出超過 3.0 的過載條件（布林遮罩）
overload_mask = current > 3.0

# 2. 畫出原本的電流折線圖
plt.plot(time, current, label='Current (A)', color='blue', marker='o')

# 3. 關鍵突破：只把「過載的時間點」與「過載的電流值」抓出來畫紅點！
plt.scatter(time[overload_mask], current[overload_mask], 
            color='red', s=150, zorder=5, label='Overload Warning')

plt.axhline(y=3.0, color='r', linestyle='--', label='Limit (3.0A)') # 3.0A 警戒線
plt.legend()
plt.grid(True)
plt.show()