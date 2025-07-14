import datetime

month = int(input("What is the month of your birth?"))
day = int(input("What is the day of your birth?"))

today = datetime.date.today()
current_year = today.year

next_birthday = datetime.date(current_year, month, day)

if next_birthday < today:
    next_birthday = datetime.date(current_year + 1, month, day)

left_days = (next_birthday - today).days

print(f'The date of your next birthday: {next_birthday}.')
print(f'{left_days} left')