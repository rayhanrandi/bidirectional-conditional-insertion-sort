import time 
import dataset
from sorters import BCIS, CountingSort


# Set up
bcis = BCIS()
counting_sort = CountingSort()
dataset = dataset.generate()


if __name__ == '__main__':

    print(
        '''
        Rayhan Putra Randi
        2106705644
        DAA - A, Kode Asdos - 1
        ''')

    # Evaluate
    for k in dataset.keys():
        # Counting Sort array
        arr = dataset[k]
        # BCIS array
        bcis_arr = arr
        comparator = sorted(arr)

        arr_preview = str(bcis_arr[:3])[:-1] + ', ... , ' + str(bcis_arr[-3:])[1:]

        print(f'Test data: {k} ({arr_preview})')

        # Run BCIS
        print('(BCIS) Sorting...')

        start_time = time.time()
        bcis.sort(bcis_arr)  # sorts in-place
        end_time = time.time()

        print('(BCIS) Sorted -> ', comparator == bcis_arr)
        bcis_elapsed = (end_time - start_time) * 1000  # to ms

        # Run Counting Sort
        print('(Counting Sort) Sorting... ')

        start_time = time.time()
        cs_arr = counting_sort.sort(arr)  # not in-place
        end_time = time.time()

        print('(Counting Sort) Sorted -> ', comparator == cs_arr)
        cs_elapsed = (end_time - start_time) * 1000  # to ms

        print(f'BCIS Runtime: {bcis_elapsed} ms.')
        print(f'CS Runtime: {cs_elapsed} ms.')
        print('Done.\n')
        
    