import Library

book_list = [
    Library.Book("The Catcher in the Rye", "J. D. Salinger", 1945, 10, False, 214),
    Library.Book("The Captain's Daughter", "Pushkin", 1836, 24, False, 124),
    Library.Book("Fight Club", "Chuck Palahniuk", 1996, 30, False, 224),
    Library.Book("The Truth about UFOs and other weird stuff", "Unknown", 2015, 999, True, 3)
]

print("Books info:\n---------\n")
for i in book_list:
    i.get_info()

most_expensive = book_list[0].most_expensive(book_list)
print(f"The most expensive book is:\n{most_expensive.title}\n")

book_list[-1].set_stoplist(False)

book_list[2].censor("Chuck Palahniuk", True)

print("Books info:\n---------\n")
for i in book_list:
    i.get_info()