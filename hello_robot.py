#practice
robot_motor = {
    "Motor1": {
        "current": 1.5, 
        "voltage": 12.0
    },
    "Motor2": {
        "current": 2.0,
        "voltage": 10.0
    }
}
for motor_specs in robot_motor:
    motor = robot_motor[motor_specs]
    power = motor["current"] * motor["voltage"]
    print(f"{motor_specs} Power: {power} Watts")
