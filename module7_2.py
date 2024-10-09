def custom_write(file_name, string):
    file_dict = {}
    file = open(file_name, 'a', encoding='utf-8')

    for i in range(0, len(string)):
        file_dict[(i+1, file.tell())] = string[i]
        file.write(string[i] + '\n')
    file.close()
    return file_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text.txt', info)

for elem in result.items():
    print(elem)
