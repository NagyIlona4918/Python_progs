import random

concepts = [
    'majorság',
    'hűbéres',
    'jobbágy',
    'nemes',
    'tized',
    'kilenced',
    'robot',
    'szügyhám',
    'vetésforgó',
    'ugar',
    'lovag'
]

definitions = [
    'Egy-egy nagybirtok vagy valamely részének igazgatási központja.',
    'Aki örökletes használatra megkapja a földet.',
    'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.',
    'Kiváltságos réteg.', 'Egyházi adó.',
    'Földesúrnak beszolgáltatott adó.',
    'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.',
    'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.',
    'A termőföld használata évszakonként más és más.',
    'Művelés alá nem vont terület.',
    'Vagyonos katonai szolgálattevő lóval, páncéllal.'
]

def quiz(concepts, definitions):
    pairs = {concept: definition for concept, definition in zip(concepts, definitions)}

    right_answers = 0
    mistakes = 0

    while pairs:
        choosed_concept = random.choice(list(pairs.keys()))
        choosed_definition = pairs[choosed_concept]

        print(f'The definition is: {choosed_definition}')
        answer = input("Which is the concept for this definition? (Type 'end', 'q' or 'quit' to stop.)")

        if answer.lower().strip() in ['end', 'q', 'quit']:
            break

        if answer.lower().strip() == choosed_concept.lower():
            print("Right!")
            right_answers += 1
        else:
            print(f"You're wrong. The right concept is: {choosed_concept}")
            mistakes += 1

        del pairs[choosed_concept]

    total = right_answers + mistakes
    print(f"You have {right_answers} right answer(s).")
    print(f"You have {mistakes} mistake(s).")

    if total > 0:
        percentage = round((right_answers / total) * 100, 2)
        print(f'Your result is {percentage:.2f}%.')
    else:
        print("You did not answer.")

quiz(concepts, definitions)