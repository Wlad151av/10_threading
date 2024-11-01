from queue import Queue   # Для имитации ожидания гостей импортируем класс Очередь
import threading # потоки позволяют независимо и одновременно питаться гостям
import time     # время ожидания или приема пищи может быть измерено
from random import randint  # генерировать промежутки времени случайной длительности

class Table:    # создание экземпляра стола подразумевает его номер и то, что он пуст

    def __init__(self,tbl_num = 1,guest = None):
        self.number = tbl_num
        self.guest = guest
        

class Guest(threading.Thread):

    def __init__(self,g_name):
        super().__init__()
        self.name = g_name

    def run():
        wait_time = randint(3,10)
        time.sleep(wait_time)

class Cafe:

    def __init__(self,*args):
        self.queue = Queue()
        self.busy_tables = 0
        self.tables = []
        for tabl in args:
            tables.append(tabl)

    def guest_arrival(self,*guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {free}')
                    self.busy_tables += 1
                    break
                else:
                    queue.put(guest.name)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):       # Обслуживание гостей
        while (not self.queue.empty()) or (self.busy_tables > 0):
            for self.guest in self.guests:  # переберем гостей - вдруг кому-то пора?
                if not self.guest.is_alive:
                    print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                    tables[table_num].guest = None
                    print(f'Стол номер {tab_num} свободен')
            for table in self.tables: # переберем столы - вдруг есть пустые?
                if tables[table_num].guest == None:
                    thread_guest = queue.get()
                    tables[table_num].guest = thread_guest
                    print(f'{thread_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tab_num}')
                    thread_guest.start()
    
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

print('Конец программы')      
