#funtion
#定義
def calculate_safety_factor(yield_strength,applied_stress):
    import math #需要數學符號時須使用,如pi
    #算 sf
    safety_factor = yield_strength / applied_stress
    return safety_factor

#應用
safety_factor = calculate_safety_factor(100, 50) #從這改參數
print(f'Safety Factor: {safety_factor}')