#practice
# 輪胎材質壽命極限字典 (磨損率超過這個百分比就必須強迫進站)
tire_specs = {
    "Soft": 60,    # 軟胎磨損大於 60% 就完蛋
    "Medium": 75,  # 中性胎壽命極限 75%
    "Hard": 85     # 硬胎壽命極限 85%
}

# 目前賽車上的四條輪胎即時狀況
current_car_status = {
    "type": "Medium",  # 目前車上裝的是中性胎
    "wear_percentage": {
        "Front-Left": 72,
        "Front-Right": 76,  # 噢不，這條磨損超標了
        "Rear-Left": 68,
        "Rear-Right": 69
    }
}

for tire, wear in current_car_status["wear_percentage"].items():
    if wear > tire_specs[current_car_status["type"]]:
        print(f"{tire} tire wear is {wear}%, which exceeds the limit for {current_car_status['type']} tires. Pit stop required!")
    else:
        print(f"{tire} tire wear is {wear}%, which is within the safe limit for {current_car_status['type']} tires.")