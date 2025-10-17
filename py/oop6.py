class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError(
                "Θερμοκρασία κάτω από το απόλυτο μηδέν δεν μπορεί να υπάρξει."
            )
        self._celsius = value


t = Temperature(25)
print(t.get_celsius())  # 25
t.set_celsius(30)
print(t.get_celsius())  # 30
