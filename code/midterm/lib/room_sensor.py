class RoomSensor :
    def __init__(self, name, temperature, humidity, light) -> None :
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self) :
        print(f"Sensor : {self.name}")
        print(f"Temperature : {self.temperature}")
        print(f"Humidity : {self.humidity}")
        print(f"Light : {self.light}")
    
    def comfort_level(self) :
        if (20 <= self.temperature <= 26) and (40 <= self.humidity <= 60) :
            return "Comfortable"
        elif (30 <= self.temperature) or (70 <= self.humidity) :
            return "Warning"
        else :
            return "Normal"
        
    def light_status(self) :
        if self.light < 200 :
            return "Dark"
        elif 200 <= self.light :
            return "Bright"