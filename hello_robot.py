#practice
# 實驗做完後，得到的 8 筆工件最大承受應力數據 (單位: MPa)
raw_stresses = [250, 420, 180, 510, 310, 480, 150, 620]

classified_data = {
    "Low_Stress": [],    # 用來放小於 300 的數據
    "Medium_Stress": [], # 用來放 300 到 500 之間的數據 (包含 300 和 500)
    "High_Stress": []    # 用來放大於 500 的數據
}

for stress in raw_stresses:
    if stress < 300:
        classified_data["Low_Stress"].append(stress)
    elif 300 <= stress <= 500:
        classified_data["Medium_Stress"].append(stress)
    else:
        classified_data["High_Stress"].append(stress)
print(classified_data)