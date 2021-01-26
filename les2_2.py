my_list = [int(a) for a in input('Enter some digits with "space": ').split()]
for a in range(1, len(my_list), 2):
    my_list[a - 1], my_list[a] = my_list[a], my_list[a - 1]
    print(' '.join([str(a) for a in my_list]))
