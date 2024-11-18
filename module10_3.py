import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for i in range(100):
            dep = (random.randint(50, 100))
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс:{self.balance}')
            time.sleep(0.001)
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
    def take(self):
        for i in range(100):
            request = (random.randint(50, 100))
            print(f'Запрос на {request}')
            if request <= self.balance:
                self.balance -= request
                print(f'Снятие: {request}. Баланс: {self.balance}')
            elif request > self.balance:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


Sber = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(Sber,))
th2 = threading.Thread(target=Bank.take, args=(Sber,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {Sber.balance}')