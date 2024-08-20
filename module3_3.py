def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25)

print_params(c=[1,2,3])

values_list = [False, 'Hello World', -300000]

values_dict = {'a': 'Computer Science', 'b': 3212, 'c': [1, 3, 5]}

print_params(*values_list)

print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)

