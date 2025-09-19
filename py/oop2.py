class DigitalCounter:
    def __init__(self, max_value=10):
        self.count = 0
        self.max_value = max_value

    def set_max(self, value):
        self.max_value = value

    def increment(self):
        self.count += 1
        if self.count > self.max_value:
            self.count = 0

    def clear(self):
        self.count = 0
