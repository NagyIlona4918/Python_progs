text = input("Please, write a password!")

def checking(text):
    db = 0 #számolja a feltételek teljesülését
    if len(text) >= 8:
        db += 1
    else:
        print("Your password needs to be at least 8 character.")
    digitcheck = None
    for character in text:
        if character.isdigit():
            digitcheck = True
            break
    if digitcheck:
        db += 1
    else:
        print("Your password needs to contain at least one digit.")

    if text != text.lower():
        db += 1
    else:
        print("Your password needs to contain at least one uppercase letter.")

    if text != text.upper():
        db += 1
    else:
        print("Your password needs to contain at least one lowercase letter.")
    if db < 4:
        print("This password is weak.")
    else:
        print("This password is strong.")
checking(text)
    
