import random
import math
import datetime
import statistics

def number_analysis():

    today = datetime.date.today()
    week_day = datetime.date.today().isoweekday()
    year_day = today.timetuple().tm_yday
    print(f'Date of today is: {today}')
    print(f'Today is {week_day}. day of this week.')
    print(f'Today is {year_day}. day of this year.')

    random_numbers = random.sample(range(1, 101), 10)

    mean = statistics.mean(random_numbers)
    sd = statistics.stdev(random_numbers)
    minimum = min(random_numbers)
    maximum = max(random_numbers)
    sqrt_of_sum = math.sqrt(sum(random_numbers))
    chosen_number = random.choice(random_numbers)

    print(f'Mean: {mean}, sd: {sd}, min: {minimum}, max: {maximum}, sqrt of sum: {sqrt_of_sum}')

    if chosen_number < 2:
        return False
    for i in range(2, int(math.sqrt(chosen_number)) + 1):
        if chosen_number % i == 0:
            return False
    print("Lucky number is prim!")
    return True


number_analysis()