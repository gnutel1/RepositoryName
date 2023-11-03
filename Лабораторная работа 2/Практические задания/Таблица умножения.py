  # Размер таблицы умножения
for x in range(2, 10):
    for y in range(2, 10):
        result = x * y
        end = " " if y != 9 else ""
        print(f"{result:2}", end=end)
    print()
