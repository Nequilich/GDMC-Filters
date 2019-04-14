import random

cityName1 = [
    "Spring", "Summer", "Green", "Man", "Ports", "Wimble", "North", "Nor", "South", "West", "Wes", "East", "Hunts", "Ox", "Liver", "Bird", "Rad", "Ash", "Wor", "Tur", "Kirk", "Chester", "Beau", "Rich", "Bos", "Wat", "Por", "Kirk", "Gaston", "New", "Ax", "Jones", "Lass", "Dan"
]
cityName2 = [
    "ville", "town", "ton", "ing", "hill", "ford", "ham", "field", "sea", "chester", "bury", "stead", "dale", "pool", "wick", "worth", "port", "view", "cliffe", "ley"
]

def getCityName():
    cityName = random.choice(cityName1) + random.choice(cityName2)

    return cityName