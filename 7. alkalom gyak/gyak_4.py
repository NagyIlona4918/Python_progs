def statistics(filenames):
    result = {}

    for name in filenames:
        if '.' in name:
            ext = name.rsplit('.', 1)[-1].lower()
            if ext in result:
                result[ext] += 1
            else:
                result[ext] = 1

    return result

print(statistics(['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY',
'biro.gib.maxpont.py', 'russian-driving-fails.mp4']))
