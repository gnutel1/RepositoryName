list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min_value_index = list_[0]

# TODO заменить на enumerate
for pos, value in enumerate(list_):

    if value <= min_value_index:
        x = value
        y = pos


print("Минимальный элемент =", x, "находится по индексу", y)