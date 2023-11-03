list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
ll=0
t = list_numbers[ll]
for x,y in enumerate(list_numbers):
    if y >= t:
        t = y
        ll = x
# TODO Поменяйте местами значения согласно условию
list_numbers[ll], list_numbers[-1] = list_numbers[-1], list_numbers[ll]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
