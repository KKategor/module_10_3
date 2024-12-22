# Task "Банковские операции"

import threading
import random
import time


class Bank:
    balance = 0
    lock = threading.Lock()
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range (10):
            self.adding = random.randint(50, 500)
            self.balance += self.adding
            print(f'Пополнение: {self.adding}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def  take(self):
        for i in range(10):
            self.withdrawal = random.randint(50, 500)
            print(f'Запрос на снятие {self.withdrawal}')
            if self.balance >= self.withdrawal:
                self.balance -= self.withdrawal
                print(f'Снятие: {self.withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)





bk = Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')



