l = [2, 44.4, True, False, 'Ilia', 1, 'apple', 'hey', 'Scott']

string_count = 0

for i in l:
    if type(i) == str:
        string_count += 1
        print(f"{string_count}: {i}")
        