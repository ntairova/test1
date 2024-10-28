numbers = [1, 6, 3, 44, 2, 13]
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(numbers)

