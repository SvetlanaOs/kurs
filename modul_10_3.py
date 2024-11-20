from random import randint
import threading
import time

lock = threading.Lock()
class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            y = randint(50, 500)
            self.balance += y
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {y}. Баланс: {self.balance}')
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            x = randint(50,500)
            print(f'Запрос на {x}')
            if x <= self.balance:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')