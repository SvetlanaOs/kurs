first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(i[0]) - len(i[1]) for i in list(zip(first,second)) if len(i[0]) != len(i[1]))
second_result = (len(second[i]) == len(first[i]) for i in range(3))

print(list(first_result))
print(list(second_result))