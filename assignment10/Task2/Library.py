class Book:

    def __init__(self, title, author, year, price, stoplist, pages):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        self.pages = pages

    def get_info(self):
        print(f"{self.title} by {self.author}\nPublished in {self.year}\nOn stoplist: {self.stoplist}\nPrice: {self.price}$\n")

    def most_expensive(self, list):
        max = 0

        for book in list:
            if book.price > max:
                max = book.price
                most_expensive = book
        return most_expensive

    def set_stoplist(self, boolean):
        self.stoplist = boolean

    def censor(self, author, boolean):
        if self.author == author:
            self.stoplist = boolean