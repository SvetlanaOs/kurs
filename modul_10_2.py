import threading
import time

class Knight(threading.Thread):
    def __init__(self,name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        x = 100
        while x > 0:
            time.sleep(1)
            x = x - self.power
            day += 1
            print(f'{self.name} сражается {day} дней (дня), осталось {x if x>=0 else 0} воинов')

        print(f'{self.name} одержал победу спустя {day} дней (дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 15)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
