from multiprocessing import Pool
import time
from tkinter.scrolledtext import example


def read_info(name):
    all_data = []
    with open (name, encoding = 'utf = 8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]
start = time.time()
for name in filenames:
    read_info(name)
finish = time.time()
result1 = finish - start
print(f'{(result1)} (линейный)')


if __name__ == '__main__':
    start = time.time()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    finish = time.time()
    result1 = finish - start
    print(f'{(result1)} (многопроцессорный)')