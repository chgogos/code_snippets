import uuid


class Connection:
    def __init__(self):
        self.code = str(uuid.uuid4()).split("-")[0]
        print(f"Η σύνδεση {self.code} άνοιξε.")

    def __del__(self):
        print(f"Η σύνδεση {self.code} έκλεισε.")


def demo():
    c1 = Connection()
    c2 = Connection()
    c3 = Connection()
    print("Εκτελείται εργασία...")

    del c2
    print("Μία σύνδεση διαγράφηκε.")


demo()
print("Η λειτουργία demo ολοκληρώθηκε.")