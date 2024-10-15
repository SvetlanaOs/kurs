import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)

    def __int__(self):
        return f'{self.age}'


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in (self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = nickname

    def register (self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print (f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password,age)
        self.users.append(new_user)
        self.current_user = new_user
    def log_out(self):
        self.current_user = None
    def add (self,*args):
        for X in args:
            F = False
            for Y in self.videos:
                if X.title == Y.title:
                    F = True
            if F == False:
                self.videos.append(X)

    def get_videos (self, word):
        films = []
        for X in self.videos:
            if word.upper() in X.title.upper():
                films.append(X.title)
        return films
    def watch_video (self, title):
        if self.current_user:
            for X in self.videos:
                if title == X.title and X.adult_mode and self.current_user.age < 18:
                    print ('Вам нет 18 лет, пожалуйста покиньте страницу')
                elif title == X.title:
                    for i in range (X.time_now + 1, X.duration + 1):
                        print (i, end = ' ')
                        X.time_now +=1
                        time.sleep(1)
                    X.time_now = 0
                    print ('Конец фильма')
        else:
            print ('Войдите в аккаунт, чтобы смотреть видео')
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')