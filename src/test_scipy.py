import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================
# 1. 定義物理模型：微分方程 f(t, y)
# ==========================================
def flywheel_dynamics(t, omega):
    """
    計算當前時間點的轉速加速度 d(omega)/dt
    t: 當前時間 (s) -> 即使函數內沒用到，也必須寫在第一個參數！
    omega: 當前轉速 (RPM)
    """
    omega_target = 5000.0  # 目標轉速 (RPM)
    tau = 0.5              # 時間常數 (s)
    
    # 計算這一瞬間的轉速變化率 (RPM / s)
    domega_dt = (1.0 / tau) * (omega_target - omega)
    return domega_dt

# ==========================================
# 2. 設定模擬條件與呼叫 SciPy 求解器
# ==========================================
t_span = (0, 3)          # 模擬時間範圍：0 秒到 3 秒
y0 = [0.0]               # 初始狀態：t=0 時，轉速為 0 RPM (必須是 list!)

# 建立我們希望輸出的時間點，讓畫出來的曲線滑順
t_eval = np.linspace(0, 3, 100) 

# 呼叫 solve_ivp 解微分方程
sol = solve_ivp(
    fun=flywheel_dynamics, 
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
plt.plot(sol.t, sol.y[0], label='Flywheel Speed', color='crimson', linewidth=2.5)
plt.axhline(y=5000, color='gray', linestyle='--', label='Target Speed (5000 RPM)')

# 標記 1 個時間常數 (1 Tau) 的位置
plt.axvline(x=0.5, color='orange', linestyle=':', label='1 Tau (63.2% Speed)')

plt.title('FRC Flywheel Spin-Up Dynamics (1st-Order ODE)')
plt.xlabel('Time (s)')
plt.ylabel('Rotational Speed (RPM)')
plt.grid(True)
plt.legend()
plt.show()