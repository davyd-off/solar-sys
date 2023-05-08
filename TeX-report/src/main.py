import random

with open("numbers.txt", "w") as f:
    for i in range(15):
        f.write(f"{random.randint(-50, 49)} ")

with open("numbers.txt", "r") as inp:
    sum = 0
    n = 0
    for line in inp:
        nums = line.split()
        for num in nums:
            num = int(num)
            if num % 2 == 0:
                sum += num
            else:
                n += 1

with open("result.txt", "w") as out:
    out.write(f"Сумма четных элементов: {sum}\n")
    out.write(f"Количество нечетных элементов: {n}\n")
