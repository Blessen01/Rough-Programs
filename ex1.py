
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Publisher: {self.name}")


# Derived class from Publisher
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # Invoke base class constructor
        self.title = title
        self.author = author

    def display(self):
        super().display()  # Call Publisher's display
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Derived class from Book
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # Invoke Book constructor
        self.price = price
        self.no_of_pages = no_of_pages

    # Method overriding
    def display(self):
        super().display()  # Call Book's display
        print(f"Price: ₹{self.price}")
        print(f"Pages: {self.no_of_pages}")


# Example usage
python_book = Python(
    name="TechPress",
    title="Mastering Python",
    author="A. Kumar",
    price=599,
    no_of_pages=350
)

python_book.display()

