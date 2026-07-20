import numpy as np

# 建立兩組數據
motor_current = np.array([1.2, 2.5, 4.8, 3.1, 0.5])

print("maximum：", np.max(motor_current))
# 結果會是：4.8

print("average：", np.mean(motor_current))
# 結果會是：2.56

#找出大於3.0的電流
print("大於3.0的電流：", motor_current[motor_current > 3.0])

#找出第幾次大於3.0
print("大於3.0的電流索引：", np.where(motor_current > 3.0)[0])