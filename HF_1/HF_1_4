numbers = []
number = input("Please, write some number!")

while number != "":
    numbers.append(number)
    number = (input("Please, write some number! If these are enough, press ENTER without a number!"))

uniques = sorted(set(numbers)) #kiválogatja az előforduló értékeket
max = 0
modus = [] #több móduszhoz

print("Your numbers' frequencies are:")
for unique in uniques:
    db = 0
    for number in numbers:
        if unique == number:
            db += 1 #megszámolja, hányszor talál egyező számot a megadott számsorból
    print(f'{unique} {db}') #gyakorisági eloszlás
    if db > max:
        max = db
        modus = [unique] #a legmagasabb db számot keresi
    elif db == max:
        modus.append(unique) #az is lehet, hogy már van ilyen, akkor több módusz van
if len(modus) == len(uniques):
    print("There is no modus.") #nem értelmezhető
    
else: 
    print(f"The modus is(are) {', '.join(modus)}, which(es) appear(s) {max} times.")
