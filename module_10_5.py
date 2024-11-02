#import os
#print(os.cpu_count())
#import multiprocessing
import datetime
import time
from threading import Thread

class C1(Thread):
    def run(self):
        time.sleep(1)

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.lock()

    def increment(self):
        with self.lock:
            self.count += 1

def worker(counter):
    for _ in range(100000):
        counter.increment()

counter = Counter()

threads = []
for _ in range(10):
    thread = threading.Thread(target = increment)

def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        time.sleep(2)
        print(letter)
    
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)

start_time = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
used_time = time.time() - start_time
print(used_time)

#read_info,filnam)
#counter = 0
#filenames = [f'./file {number}.txt' for number in range(1, 5)]
#def first_worker(n):
#    global counter
#    for i in range(n):
 #       counter += 1
 #       time.sleep(1)
 #   print('Первый подход линейный вызов', counter)
#all_data = []
    
'''def read_info(name):
    global all_data
    i = 0
    with open(name,'r') as source:
        all_data.append(source.readline())
           

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
i = 1
for filnam in filenames:
    thread[i] = threading.Thread(read_info,filnam)
    thread[i].start()
    i += 1
finish_time = time.time()
result = finish_time - start_time
print(result)



# Многопроцессный

#process1 = multiprocessing.Process(target = read_info)
#process2 = multiprocessing.Process(target = read_info)
#process1.start()

# создаем пул процессов
pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())

# Используем многопроцессорный пул для обработки данных
results = pool.map(worker, data)

# Завершаем пул
pool.close()
pool.join()

# if __name__ == '__main__':
     
#     with Pool:
#        map(read_info,filenames)'''
