#practice
robot_motor =[
    {
        "name": "Motor1",
        "current": 1.5
    },
    {
        "name": "Motor2",
        "current": 2.0
    }
]
for motor in robot_motor:
    if motor["current"] >= 2.0:
        print(f"{motor['name']} is drawing too much current: {motor['current']}A")
    else:
        print(f"{motor['name']} is operating within safe limits: {motor['current']}A")