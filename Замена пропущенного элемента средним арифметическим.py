numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sus = sum(numbers[:4])
sas = sum(numbers[5:])
s = sus + sas
kok = len(numbers)
k = s / kok
numbers[4] = k


print("Измененный список:", numbers)
