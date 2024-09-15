def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    x = (len(string), string.upper(), string.lower())
    count_calls()
    return x


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i]=list_to_search[i].upper()
    if string.upper() in list_to_search:
        x = True
    else:
        x = False
    return x


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
