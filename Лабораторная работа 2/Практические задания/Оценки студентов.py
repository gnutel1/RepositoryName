# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]
for y in students:
    if y["grade"] > 3:
      print(f'{y ["name"]}.' , "Оценка:", y ["grade"])
# TODO Распечатать имена студентов с оценками выше тройки
