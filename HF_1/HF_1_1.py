text = input("Please, write a sentence! ").lower()
vowels = ['a', 'e', 'i', 'o', 'ö', 'u', 'ü']
vowels_found = [] #Ebben lesznek a megtalált magánhangzók
for letter in text:
    for vowel in vowels:
        if letter == vowel:
            vowels_found.append(letter) #ha magánhangzót talál, kigyűjti.

print(f"Your sentence was: {text.capitalize()} \n The vowels in your sentence are: {(", ".join(vowels_found))} \n This is {len(vowels_found)} vowels.")
