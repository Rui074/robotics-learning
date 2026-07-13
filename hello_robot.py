#practice
def check_drive_system(t_motor, gear_ratio, efficiency, mass, slope_deg, wheel_radius):
    import math
    t_output=t_motor*gear_ratio*efficiency
    t_load=mass*9.81*math.sin(math.radians(slope_deg))*wheel_radius
    SF=t_output/t_load
    return SF
#apply
SF = check_drive_system(0.5, 10, 0.85, 20, 15, 0.05)
if SF>=1.5:
    print("設計安全,馬達扭力足夠")
elif SF<1.5 and SF>1:
    print("扭力足夠但安全係數不足,建議加大減速比") 
else:
    print("馬達失速!扭力不足以爬坡") 
      