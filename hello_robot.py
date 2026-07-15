# 1. 用 class 關鍵字宣告藍圖，名字開頭通常大寫
class Motor:
    
    # 這是「初始化構造函式」── 規定馬達一出生，必須帶有什麼規格
    def __init__(self, motor_name, max_current):
        self.name = motor_name       # 馬達的名字
        self.current = 0.0           # 剛出廠時，即時電流預設為 0.0A
        self.limit = max_current     # 這顆馬達的安全電流上限值
        
    # 這是內建在馬達肚子裡的功能 (Method) ── 模擬馬達運轉運作
    def run(self, input_current):
        self.current = input_current # 更新目前電流
        print(f"[{self.name}] 正在運轉，目前電流：{self.current} A")
        
        # 直接把昨天的 if-else 自控邏輯內建進來！
        if self.current >= self.limit:
            print(f"警告：{self.name} 電流超載！上限為 {self.limit} A")
            # 2. 實例化 (Instantiation) ── 依照藍圖做出真實的馬達物件
# 這邊丟進去的參數，會直接傳給 __init__ 裡面的 motor_name 和 max_current
left_motor = Motor("Left_Drive", 3.0)   # 製造左輪馬達，限流 3.0A
arm_motor = Motor("Arm_Lift", 2.0)      # 製造手臂馬達，限流 2.0A

# 3. 叫它們各自做動作！用「點 .」來呼叫功能
print("--- 機器人啟動 ---")
left_motor.run(1.5)  # 給左輪 1.5A 電流
arm_motor.run(2.5)   # 給手臂 2.5A 電流（這會觸發超載警告！）