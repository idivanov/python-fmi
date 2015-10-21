def interpret_western_sign(day, month):

    signs = [
        ('aquarius', 21),
        ('pisces', 19),
        ('aries', 21),
        ('taurus', 21),
        ('gemini', 21),
        ('cancer', 21),
        ('leo', 23),
        ('virgo', 23),
        ('libra', 23),
        ('scorpio', 23),
        ('sagittarius', 22),
        ('capricorn', 22)
    ]

    return signs[month - 1][0] if day >= signs[month - 1][1] \
        else signs[month - 2][0]


def interpret_chinese_sign(year):

    signs = [
        "rat",
        "ox",
        "tiger",
        "rabbit",
        "dragon",
        "snake",
        "horse",
        "sheep",
        "monkey",
        "rooster",
        "dog",
        "pig"
    ]

    return signs[(year-1900) % 12]


def interpret_both_signs(day, month, year):
    return (interpret_western_sign(day, month), interpret_chinese_sign(year))
