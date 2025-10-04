class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return (
            f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"
        )


b = Book("1984", "George Orwell", 9.99)

print(b)  # Uses __str__: '1984' by George Orwell
print(str(b))  # Uses __str__: "'1984' by George Orwell"
print(
    repr(b)
)  # Uses __repr__: "Book(title='1984', author='George Orwell', price=9.99)"
