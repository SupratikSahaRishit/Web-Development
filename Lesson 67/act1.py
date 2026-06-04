class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'"{self.title}" has been borrowed.')
        else:
            print(f'"{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not borrowed.')

book1 = Book("Wimpy kid", "Jeff Kinney")
book2 = Book("Lion boy", "Zizou Corder")
book3 = Book("The Red Headed League", "Arthur Conan Doyle")

book1.borrow()
book2.borrow()
book3.borrow()
print()
book1.return_book()
book2.return_book()
book3.return_book()