def all_variants(text):
    length = len(text)

    for i in range(length):
        yield text[i]

    for i in range(length - 1):
        yield text[i:i + 2]

    for i in range(length - (length - 1)):
        j = length
        yield text[i:j]


a = all_variants("abc")
for i in a:
    print(i)
