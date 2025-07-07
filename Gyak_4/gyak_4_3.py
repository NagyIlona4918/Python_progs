def course_code_grouping(text):
    if text == "":
        return {}

    courses = text.split(';')
    groups = {'infos': [], 'matekos': [], 'szabval': []}

    for code in courses:
        if code.startswith('I'):
            groups['infos'].append(code)
        elif code.startswith('M'):
            groups['matekos'].append(code)
        elif code.startswith('X'):
            groups['szabval'].append(code)

    return groups

print(course_code_grouping("IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E"))
