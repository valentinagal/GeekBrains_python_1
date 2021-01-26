the_str = input("Enter some string: ")
the_word = []
num = 1
for el in range(the_str.count(' ') + 1):
    the_word = the_str.split()
    if len(str(the_word)) <= 10:
        print(f'{num} {the_word[el]}')
        num += 1
    else:
        print(f'{num} {the_word[el][0:10]}')
        num += 1
