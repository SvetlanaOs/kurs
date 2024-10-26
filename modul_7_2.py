def custom_write(file_name, strings):
    file = open (file_name, 'w', encoding = 'utf-8')
    k = 1
    strings_position = {}
    for i in strings:
        x = file.tell()
        strings_position [(k , x)] = i
        file.write(f'{i}\n')
        k+=1
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)