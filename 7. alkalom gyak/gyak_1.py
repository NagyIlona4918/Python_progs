def month_len():
    month = int(input("Write the number of a month! "))
    lengths = []

    for i in range(1, 13):
        if i == 2:
            lengths.append(28)
        elif (i <= 7 and i % 2 != 0) or (i >= 8 and i % 2 == 0):
            lengths.append(31)
        else:
            lengths.append(30)

    print(f'The number of days of your months are {lengths[month - i]}')

month_len()
