seasons = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

month = int(input('Enter number of your favourite month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
