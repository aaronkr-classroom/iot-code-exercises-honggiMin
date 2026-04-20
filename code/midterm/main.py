from lib.room_sensor import RoomSensor

sensorsList = [
    RoomSensor("Kitchen", 23, 53, 230),
    RoomSensor("Bedroom", 27, 40, 150),
    RoomSensor("Balcony", 36, 80, 300)
]

bonus = {"Comfortable" : 0, "Normal" : 0, "Warning" : 0}

for i in sensorsList :
    i.show_info()

    cl = i.comfort_level()
    ls = i.light_status()

    print(f"Comfort Level : {cl}")
    print(f"Light Status : {ls}\n")

    bonus[cl] += 1

print("total")
for name,value in bonus.items() :
    print(f"{name}: {value}")