class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def turn_on(self):
        return f"Η συσκευή {self.brand} ισχύος {self.power}W ενεργοποιήθηκε."

    def __repr__(self):
        return f"Device(brand={self.brand}, power={self.power})"


class Laptop(Device):
    def __init__(self, brand, power, battery_life):
        super().__init__(brand, power)
        self.battery_life = battery_life

    def turn_on(self):
        return f"Ο φορητός υπολογιστής {self.brand} ενεργοποιήθηκε."

    def __repr__(self):
        return f"Laptop(brand={self.brand}, power={self.power},battery_life={self.battery_life})"


class TV(Device):
    def __init__(self, brand, power, screen_size):
        super().__init__(brand, power)
        self.screen_size = screen_size

    def turn_on(self):
        return f"Η τηλεόραση {self.brand} {self.screen_size} ενεργοποιήθηκε"

    def __repr__(self):
        return f"TV(brand={self.brand}, power={self.power}, screen_size={self.screen_size})"


d1 = Device("Philips", 100)
l1 = Laptop("Dell", 65, 10)
t1 = TV("Samsung", 150, 55)
print(d1)
print(d1.turn_on())
print(l1)
print(l1.turn_on())
print(t1)
print(t1.turn_on())
