import dataset
import bcis, counting_sort
import time 


dataset = dataset.generate()


if __name__ == '__main__':

    start_time = time.time()
    
    print(counting_sort.sort(dataset['kecil_randomized']))\
    # print(sorted(dataset['kecil_reversed']))
    
    end_time = time.time()
    
    elapsed = (end_time - start_time) * 1000  # to ms
    print(f'execution time: {elapsed} ms')