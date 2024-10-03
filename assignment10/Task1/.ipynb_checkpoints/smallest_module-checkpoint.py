def find_two_smallest(list):
    first = min(list)
    list_without_first = []

    for i in list:
        if i > first:
            list_without_first.append(i)

    second = min(list_without_first)
    
    return first, second