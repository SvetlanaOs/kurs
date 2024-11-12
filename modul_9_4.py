import random

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)
    def __call__(self):
        return random.choice(self.words)
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w', encoding = 'utf-8')
        for i in data_set:
            file.write(str(i) + '\n')
        file.close()

    return write_everything
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y : x == y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())