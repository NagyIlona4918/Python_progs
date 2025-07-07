def text_analyze(text):
    result = {"letter": 0, "digit": 0, "other": 0}
    
    for character in text:
        if character.isalpha():
            result["letter"] += 1
        elif character.isdigit():
            result["digit"] += 1
        else:
            result["other"] += 1
    
    return result

print(f'The result of your text is: {text_analyze("Ez egy 5 szavas szöveg.")}')
