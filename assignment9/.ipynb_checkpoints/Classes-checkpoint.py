current_year = 2024

class Animal:
    def __init__(self, genus, name, year_of_birth, nickname, is_programmer):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.nickname = nickname
        self.is_programmer = is_programmer

    def get_age(self, year):
        age = year - self.year_of_birth
        return age

    def get_info(self):
        print(f"{self.name} is a/an {self.genus}. Also known as {self.nickname}.")

    def check_programmer(self):
        if self.is_programmer == True:
            print(f"{self.name} is a programmer.")
        else:
            print(f"{self.name} is not a programmer.")


friends = [
 Animal("python", "Billy", 1984, "Bongo", True),
 Animal("elephant", "Dumbo", 1990, "Dumby", True),
 Animal("fox", "Foxy", 2002, "Orange", False),
]


for friend in friends:    # Run all methods on friends (sorry, friends)
    friend.get_info()
    print(f"Age: {friend.get_age(current_year)}")
    friend.check_programmer()
    print("\n")

def find_oldest(animals, year):
    max_age = 0

    for animal in animals:
        age = animal.get_age(year)
        if age > max_age:
            max_age = age
            oldest_animal = animal

    return oldest_animal

oldest = find_oldest(friends, current_year)

print(f"The oldest animal is a/an {oldest.genus}, named {oldest.name}, he is {current_year - oldest.year_of_birth}.")


def write_animals(animals, file_name):
    file = open(file_name, 'w')

    for animal in animals:
        file.write(f"{animal.name}, {animal.genus}\n")

    file.close()

write_animals(friends, "friends.txt")