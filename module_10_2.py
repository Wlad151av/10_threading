import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_num = 100
        self.days = 0


    def run(self):

        print(f'{self.name}, на нас напали!')
        while self.enemy_num > 0:
            self.days += 1
            time.sleep(1)
            self.enemy_num -= self.power
            print(f'{self.name} сражается {self.days} день(дня, дней)..., осталось {self.enemy_num} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
