import threading
from random import randint
from threading import Thread
from threading import Lock
from time import sleep

class Bank:

    balance = 1000
    lock = Lock()
    
def __init__(self):
    balance = 0

def deposit(self):
    oper_num = 100
    while oper_num>0:
        income = randint(50,500)
        self.balance += income
        print(f'Пополнение:{income}. Баланс: {balance}')
        if balance >= 500 and lock.locked():
            lock.release()
        oper_num -= 1    
    time.sleep(0.001)        

def take(self):
    oper_mun = 100
    while oper_mun>0:
        outcome = randint(50,500)
        if outcome <= balance:
            balance -= outcome
            print(f'Снятие:{outcome}. Баланс: {balance}')
        else:
            print('Запрос отклонён, недостаточно средств')
            lock.acquire()
        oper_mun -= 1    
    time.sleep(0.001)  
    

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
