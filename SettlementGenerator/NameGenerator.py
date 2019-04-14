import random

cityName1 = [
    "Spring", "Summer", "Green", "Man", "Ports", "Wimble", "North", "Nor", "South", "West", "Wes", "East", "Hunts", "Ox", "Liver", "Bird", "Rad", "Ash", "Wor", "Tur", "Kirk", "Chester", "Beau", "Rich", "Bos", "Wat", "Por", "Kirk", "Gaston", "New", "Ax", "Jones", "Las", "Dan"
]
cityName2 = [
    "ville", "town", "ton", "ing", "hill", "ford", "ham", "field", "sea", "chester", "bury", "stead", "dale", "pool", "wick", "worth", "port", "view", "cliffe", "ley"
]

def getCityName():
    cityName = random.choice(cityName1) + random.choice(cityName2)

    return cityName

def assignSectionNames(sections):
    name1 = cityName1.copy()
    name2 = cityName2.copy()

    random.shuffle(name1)

    for section in sections:
        section.name = name1.pop() + random.choice(name2)