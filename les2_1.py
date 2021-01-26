my_list = ['random', 3.1416, 7, False, None, 'list']


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)
