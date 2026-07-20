import numpy as np
import matplotlib.pyplot as plt  # 引入繪圖工具，習慣縮寫為 plt

# 我們的 3x4 電流數據
all_motors = np.array([
    [1.2, 1.3, 1.1, 1.2],
    [4.5, 4.8, 1.5, 1.4],
    [2.0, 2.1, 1.9, 2.0]
])

# 1. 建立圖表
plt.figure(figsize=(8, 5))  # 設定圖表寬高比為 8:5

# 2. 畫出四條馬達的電流曲線
# all_motors[:, 0] 代表取「所有時間點（列）」的「第 0 顆馬達（行）」
plt.plot(all_motors[:, 0], label="Left Front", marker='o')
plt.plot(all_motors[:, 1], label="Left Rear", marker='s')
plt.plot(all_motors[:, 2], label="Right Front", marker='^')
plt.plot(all_motors[:, 3], label="Right Rear", marker='d')

# 3. 加上圖表標籤與設計
plt.title("FRC Robot Motor Current Monitoring") # 標題
plt.xlabel("Time Step")                         # X 軸標籤
plt.ylabel("Current (Amps)")                    # Y 軸標籤
plt.xticks([0, 1, 2])                           # 強制固定 X 軸刻度為 0, 1, 2
plt.grid(True)                                  # 開啟格線
plt.legend()                                    # 顯示圖例（左前、左後...）

# 4. 秀出圖表！
plt.show()