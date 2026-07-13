#基礎語法
# 定義
yield_strength=250
applied_stress=180
#算安全係數
safety_factor=yield_strength/applied_stress
print(f'sf={safety_factor}')
#判定
if safety_factor >= 1.5:
    print('safe')
else:
    print('danger')    
