# practice

# 1. 使用 'w' (Write) 模式：打開一個檔案準備寫入。如果檔案不存在，Python 會自動幫你建立！
# with open("檔名", "模式", encoding="utf-8") as 變數:
with open("motor_log.txt", "w", encoding="utf-8") as file:
    # 2. 寫入資料，跟 print 很像，但要在最後手動加上 "\n" 來換行
    file.write("--- 機器人硬體測試紀錄 ---\n")
    file.write("Motor1 current: 1.5A\n")
    file.write("Motor2 current: 2.0A\n")
    file.write("測試結束，系統一切正常。\n")

print("📝 檔案寫入成功！快去左邊的專案資料夾看看有沒有多出 motor_log.txt！")
# 1. 使用 'r' (Read) 模式打開檔案
with open("motor_log.txt", "r", encoding="utf-8") as file:
    # 2. 用 .read() 一次把整張紙的內容讀成一個大字串
    content = file.read()
    
print("📖 讀取檔案內容如下：")
print(content)