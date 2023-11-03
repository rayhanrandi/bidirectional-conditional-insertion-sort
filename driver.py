import time 
import dataset
from sorters import BCIS, CountingSort


bcis = BCIS()
counting_sort = CountingSort()
dataset = dataset.generate()

def execute_bcis():
    pass

def execute_counting_sort():
    for input_size_type in dataset:
        print(input_size_type)
        start_time = time.time()
        print(counting_sort.sort(dataset[input_size_type]))
        end_time = time.time()
        elapsed = (end_time - start_time) * 1000  # to ms
        print(f'execution time: {elapsed} ms\n')

if __name__ == '__main__':

    arr = dataset['kecil_reversed']
    # arr = [1,2,9,3,0,47,12,4,3]
    # arr1 = [1,2,9,3,0,47,12,4,3]

    bcis.sort(arr)
    print(arr)
    print('sorted? -> ', dataset['kecil_sorted'] == arr)
    
    