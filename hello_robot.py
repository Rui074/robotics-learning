#practice
laser_readings=[10.02, 9.98, -999.0, 10.01, -999.0, 9.99]
clean_readings=[]
for reading in laser_readings:
    if reading != -999.0:
        clean_readings.append(reading)
print(clean_readings)
