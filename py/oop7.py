class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value


t = Temperature(25)
print(t.celcius)  # 25
t.celsius = 30
print(t.celcius)  # 30
