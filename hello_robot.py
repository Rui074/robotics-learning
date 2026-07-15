# practice
class Motor:
    def __init__(self, motor_name, max_current):
        self.name = motor_name
        self.current = 0.0
        self.limit = max_current
        # 新增一個屬性：記錄馬達現在是否啟動 (True 表示啟動，False 表示斷電)
        self.is_active = True 
        
    def run(self, input_current):
        # 如果已經斷電，就不准運轉！
        if not self.is_active:
            print(f"❌ 拒絕執行：{self.name} 已經被緊急斷電，無法運轉！")
            return
            
        self.current = input_current
        print(f"[{self.name}] 正在運轉，目前電流：{self.current} A")
        
        if self.current >= self.limit:
            print(f"⚠️ 警告：{self.name} 電流超載！")
            # 超載了！立刻呼叫我們肚子裡的緊急斷電功能
            self.emergency_stop()

    def emergency_stop(self):
        self.is_active = False
        self.current = 0.0

        print(f"🚨 系統：{self.name} 已強制緊急斷電！")

# 製造一個超載極限只有 2.0A 的馬達
test_motor = Motor("Lifter_Motor", 2.0)

# 正常運轉 (1.5A < 2.0A) -> 應該順利運轉
test_motor.run(1.5) 

# 超載運轉 (2.5A >= 2.0A) -> 應該觸發超載、自動呼叫緊急斷電、再拒絕下一次運轉
test_motor.run(2.5) 

# 斷電後嘗試再次運轉 -> 應該被拒絕
test_motor.run(1.0)