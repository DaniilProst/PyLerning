calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()

    return tuple([len(string), string.upper(), string.lower()])


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            return True

    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cycling']))
print(calls)
