n = int(input("Введите число от 3 до 20: "))
result = ''
for i in range(1, n // 2 + 1):
    for j in range(n, n // 2, -1):
        if i < j:
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"

print(f"Нужный пароль для числа {n}: {result}")
