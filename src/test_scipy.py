
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# 1. 定義物理模型：微分方程 f(t, y)
# ==========================================
def chassis_dynamics(t, v):
    """
    計算當前時間點的轉速加速度 dv/dt
    t: 當前時間 (s) 
    v: 車速
   """
    F = 200.0
    m = 40.0
    c = 20.0
 
    # 計算這一瞬間的轉速變化率 (RPM / s)
    dv_dt = (F / m) - (c / m) * v
    return dv_dt


# ==========================================
# 2. 設定模擬條件與呼叫 SciPy 求解器
# ==========================================
t_span = (0, 10)   # 模擬時間範圍：0 秒到 10 秒
y0 = [0.0]         # 初始狀態：t=0 時，車速為 0 

# 建立我們希望輸出的時間點，讓畫出來的曲線滑順
t_eval = np.linspace(0, 10, 200) 

# 呼叫 solve_ivp 解微分方程
sol = solve_ivp(
    fun=chassis_dynamics, 
    t_span=t_span, 
    y0=y0, 
    t_eval=t_eval
)

# ==========================================
# 3. 提取結果與視覺化
# ==========================================
# sol.t -> 時間陣列 ( shape: (100,) )
# sol.y -> 狀態陣列 ( shape: (1, 100) )，因為只有一個變數，所以取 sol.y[0]

plt.figure(figsize=(8, 5))
plt.plot(sol.t, sol.y[0], label='Chassis Speed', color='crimson', linewidth=2.5)
plt.axhline(y=10, color='gray', linestyle='--', label='Target Speed (10 m/s)')

plt.title('FRC Chassis Acceleration Dynamics (1st-Order ODE)')
plt.xlabel('Time (s)')
plt.ylabel('Linear Speed (m/s)')
plt.grid(True)
plt.legend()
plt.show()