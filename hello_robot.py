# practice
class Motor:
    def __init__(self, motor_name, max_current):
        self.name = motor_name
        self.current = 0.0
        self.limit = max_current
        self.is_active = True 
        
    def run(self, input_current):
        if not self.is_active:
            print(f"❌ 拒絕執行：{self.name} 已經被緊急斷電，無法運轉！")
            return
            
        self.current = input_current
        print(f"[{self.name}] 正在運轉，目前電流：{self.current} A")
        
        if self.current >= self.limit:
            print(f"⚠️ 警告：{self.name} 電流超載！")
            self.emergency_stop()

    def emergency_stop(self):
        self.is_active = False
        
        # 1. 先把超載時的錯誤訊息準備好
        error_msg = f"🚨 警報：{self.name} 發生電流超載！超載數值：{self.current} A (上限為 {self.limit} A)\n"
        
        # 2. 【請在這邊寫】：
        # 請用 with open 開啟一個叫 "error_log.txt" 的檔案
        # 記得要用「累加模式 ('a')」喔！這樣才不會把之前的報警紀錄洗掉。
        # 編碼請設定為 utf-8
        with open("error_log.txt", "a", encoding="utf-8") as log_file:
            # 3. 【請在這邊寫】：
            # 把上面準備好的 error_msg 寫入檔案中
            log_file.write(error_msg)
            
        self.current = 0.0
        print(f"🚨 系統：{self.name} 已強制緊急斷電，並已記錄至 log 中！")
        # 建立兩顆不同的馬達
motor_A = Motor("Axis_1_Motor", 3.0)
motor_B = Motor("Axis_2_Motor", 1.5)

# 讓它們輪流超載
motor_A.run(4.2)  # 超載！應該寫入第一筆 log
motor_B.run(2.0)  # 超載！應該寫入第二筆 log