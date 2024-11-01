import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy_num = 100
        
    def run(self):

        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemy_num >= self.power:
            time.sleep(1)
            self.enemy_num -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня, дней)..., осталось {self.enemy_num} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 11)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
