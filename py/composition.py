class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine # Σύνθεση

    def start_car(self):
        print(f"Starting {self.make} {self.model}...")
        self.engine.start()


v6_engine = Engine(300, "V6")
my_car = Car("Toyota", "Supra", v6_engine)
my_car.start_car()
