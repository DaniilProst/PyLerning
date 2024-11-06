def is_prime(func):
    def is_prime_number(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
            return True

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)
