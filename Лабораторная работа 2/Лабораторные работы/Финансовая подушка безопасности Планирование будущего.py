money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
x = 0

monts = 0
x = spend - (salary + money_capital)
money_capital = x * (-1)
while x < 0:
    monts += 1
    spend = spend*increase + spend
    x = spend - (salary + money_capital)
    money_capital = x * (-1)
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", monts)
