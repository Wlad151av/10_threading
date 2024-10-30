

from time import sleep
import threading


def write_words(word_count, file_name):
    with open(file_name,'w') as stream:
        for ind_x in range(word_count):
            sleep(0.5)
            stream.write(f'Какое-то слово № {ind_x}')
    print(f'Завершилась запись в файл: {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

tr1 = threading.Thread(target = write_words)
tr2 = threading.Thread(target = write_words)
tr3 = threading.Thread(target = write_words)
tr4 = threading.Thread(target = write_words)

tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()