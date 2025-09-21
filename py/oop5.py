class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def add_rating(self, score):
        if 1 <= score <= 5:
            self.ratings.append(score)
        else:
            print("Η βαθμολογία πρέπει να είναι από 1 έως 5.")

    def average_rating(self):
        if not self.ratings:
            return "Δεν υπάρχουν βαθμολογίες"
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        avg = self.average_rating()
        return f"Τίτλος: {self.title}, ISBN: {self.isbn}, Μέση βαθμολογία: {avg}"


book1 = Book("Ο Μικρός Πρίγκιπας", "978-960-453-083-7")
book2 = Book("Η Φόνισσα", "978-960-01-0547-7")
book1.add_rating(5);book1.add_rating(4)
book2.add_rating(4);book2.add_rating(4)
print(book1)
print(book2)
