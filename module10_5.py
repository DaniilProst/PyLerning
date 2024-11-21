import multiprocessing
from time import sleep, time


def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        for line in file:
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#start_time = time()
#x = list(map(read_info, filenames))

#end_time = time()
#print(f'{end_time - start_time}(линейный)')
if __name__ == '__main__':
    start_time = time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time()
    print(f'{end_time - start_time}(многопроцессорный)')