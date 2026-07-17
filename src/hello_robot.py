# practice

class BatteryMonitor:
    # 1. 初始化，存入最高安全溫度
    def __init__(self, max_temp=50.0):
        self.max_temp = max_temp

    # 2. 檢查電池溫度
    def check_temp(self, temp):
        # 依照你的邏輯：如果溫度在 0 到 max_temp 之間
        if 0.0 <= temp <= self.max_temp:
            print(f"✅ 電池溫度 {temp}°C 正常。")
            
            # 寫入 normal_temp.txt
            with open("normal_temp.txt", "a", encoding="utf-8") as file:
                file.write(f"{temp}\n")
                
        else:
            print(f"🚨 警告：電池溫度異常！目前溫度 {temp}°C")
            
            # 寫入 temp_alerts.txt
            with open("temp_alerts.txt", "a", encoding="utf-8") as file:
                file.write(f"ALERT: Battery temp is {temp}°C (Safe range: 0.0 ~ {self.max_temp}°C)\n")


# ==========================================
# 🏎️ 測試程式碼
# ==========================================

# 建立一個限溫 50 度的監控器
monitor = BatteryMonitor(max_temp=50.0)

# 模擬一整天的電池溫度變化
battery_temps = [25.3, 48.2, 52.5, 12.0, -2.1, 35.6]

print("--- 電池安全監控開始 ---")
for t in battery_temps:
    monitor.check_temp(t)

print("\n📝 記錄完成！請檢查 'normal_temp.txt' 與 'temp_alerts.txt'！")
