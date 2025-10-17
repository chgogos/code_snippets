class CPU:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def process(self):
        print(f"Η CPU {self.model} στα {self.speed}GHz επεξεργάζεται δεδομένα...")


class Computer:
    def __init__(self, brand, ram, cpu):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu

    def start(self):
        print(f"Εκκίνηση υπολογιστή {self.brand} με {self.ram}GB RAM...")
        self.cpu.process()


cpu = CPU("Intel i7", 3.4)
my_computer = Computer("Dell", 16, cpu)
my_computer.start()
