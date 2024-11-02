from queue import Queue   # Для имитации ожидания гостей импортируем класс Очередь
import threading # потоки позволяют независимо и одновременно питаться гостям
from time import sleep     # время ожидания или приема пищи может быть измерено
from random import randint  # генерировать промежутки времени случайной длительности

busy_tables = 0
guests_in_queue = 0
lock = threading.Lock()

class Table:    # создание экземпляра стола подразумевает его номер и то, что он пуст

    def __init__(self,i):
        self.number = i
        self.guest = None
        

class Guest(threading.Thread):

    def __init__(self,g_name):
        super().__init__()
        self.name = g_name
        self.number = None

    def run(self):  # метод run должен иметь доступ к экземпляру через self
        wait_time = randint(3,10)   #    lock.acquire()
       # print(f'У {self.name} {wait_time} времени на обед\n')
        lock.release()
        sleep(wait_time)
        lock.acquire()
        print(f'{self.name} покушал(-а) и ушёл(ушла)!')
        print(f'Стол {self.number} свободен!')
        lock.release()
                       

class Cafe:

    def __init__(self,*tables):
        self.queue = Queue()
        self.n = len(tables)  #  print(f'there are {self.n} tables')
        self.tables = []
        for table in tables:
            self.tables.append(table)  #   print(table.number)    
                       
    def guest_arrival(self,*guests):
        global busy_tables, guests_in_queue
        i = 0 # переберем столы - вдруг есть пустые?
        for guest in guests:
            if i < self.n and self.tables[i].guest == None:#  Если стол пуст - можно посадить гостя!
                self.tables[i].guest = guest.name
                lock.acquire()
                busy_tables += 1
                guest.number = i+1
                print(f'{guest.name} прибыл(-ла) и сел(-а) за стол #{i+1}. Занято {busy_tables} столов.')
                guest.start() # guest.join() # добавление потока к основному тормозит старт остальных потоков
                i += 1                 
            else:
                 self.queue.put(guest)
                 guests_in_queue += 1 #print(f'D очереди {guests_in_queue} гостей\n')

        #print('Все прибывшие гости учтены!')
        
    def discuss_guests(self):       # Обслуживание гостей
        global busy_tables, guests_in_queue
        while not self.queue.empty(): #guests_in_queue): # or (busy_tables > 0):
          #  print(f'Начнем обслуживание очереди из {guests_in_queue} гостей!\n')
            for table in self.tables: # переберем столы - вдруг есть пустые?
               # print(f'Что со столом номер {table.number}?')
                if table.guest == None:
                    guest = self.queue.get()
                    table.guest = guest.name
                    busy_tables += 1
                    guest.number = table.number
                    lock.acquire()
                    print(f'{guest.name} вышел(-ла) из очереди {guests_in_queue} и сел(-а) за стол #{table.number}')
                    guests_in_queue -= 1
                    
                    guest.start()   # lock.release()
                    break
                
                else:   # переберем гостей - вдруг кому-то пора?
                 #   print(f'Кто же занимает стол номер {table.number} ?')
                 #   print(f'Вероятно, это {table.guest}. Он (-а) скоро рассчитается и освободит стол')
                    for guest in guests:
                        if (not guest.is_alive()) and (table.guest == guest.name):
                          #  print(f'{guest.name} покушал(-а) и ушёл(ушла)\n\n') #    print(threading.enumerate())
                            table.guest = None
                            busy_tables -= 1
                            lock.acquire()
                           # print(f'\n\nЗанято {busy_tables} столов, в очереди {guests_in_queue} гостей\n\n\n')
                            if (busy_tables == 0):
                                print('Конец программы. Все гости довольны. Кафе закрывается.')
                            lock.release()
                            #  print(f'Стол номер {table.number} свободен, заняты {busy_tables} столов')    
            if guests_in_queue == 0:
                print(f'Занято {busy_tables} столов, в очереди {guests_in_queue} гостей\n')     
                    


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

#for g in guests:
   # g.join()  # добавление потока к основному тормозит старт остальных потоков
      
