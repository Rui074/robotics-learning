#dictionary
motor_spec = {
    "max_speed": 100, #rpm
    "max_torque": 50, #Nm
    "operating_voltage": 12 #V
}
print(motor_spec["max_speed"])
motor_spec["max_speed"] = 120
motor_spec["mass"] = 60
print(motor_spec)