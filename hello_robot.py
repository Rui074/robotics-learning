#practice
# 這是機械臂三個關鍵軸 (Axis1, Axis2, Axis3) 在一段時間內連續傳回的電流 List
# 資料格式：[Axis1 電流, Axis2 電流, Axis3 電流]
arm_stream = [
    [1.2, 2.1, 1.5],
    [1.3, -99.0, 1.6],  # 出現 -99.0 代表感測器斷訊壞軌！
    [1.5, 3.2, 1.4],   # 觸發大於 3.0A 的安全過載！
    [0.0, 2.0, 1.7],   # 剛好 0.0 代表可能卡死或發生奇點 (Singularity)！
    [1.1, 1.9, 1.4]
]
for idx, current in enumerate(arm_stream):
    is_safe = True
    for axis, value in enumerate(current):
        if value == -99.0:
            print(f"第 {idx+1} 筆資料: Axis{axis+1} 感測器斷訊壞軌！")
            is_safe = False
        elif value > 3.0:
            print(f"第 {idx+1} 筆資料: Axis{axis+1} 過載！電流值: {value}A")
            is_safe = False
        elif value == 0.0:
            print(f"第 {idx+1} 筆資料: Axis{axis+1} 可能卡死或發生奇點 (Singularity)！")
            is_safe = False
    if is_safe:
        print(f"第 {idx+1} 筆資料: 所有軸電流正常。")   