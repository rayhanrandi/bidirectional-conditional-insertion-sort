import os
import time 
import psutil
import dataset
from sorters import BCIS, CountingSort


# Set up
bcis = BCIS()
counting_sort = CountingSort()
datasets = dataset.generate()


if __name__ == '__main__':

    print(
        '''
        Comparing...
        ''')

    # write results to output.txt
    f = open('output.txt', "w")

    f.write(
        '''
        Rayhan Putra Randi
        2106705644
        DAA - A, Kode Asdos - 1
        \n''')
    
    # Evaluate & export used dataset
    for k in datasets.keys():
        print(
            f'''
        {k}...''', end='')
        # export
        dataset.write_to_file(f'{k}.txt', str(datasets[k]))

        # Counting Sort array
        arr = datasets[k]
        # BCIS array
        bcis_arr = arr
        comparator = sorted(arr)

        arr_preview = str(bcis_arr[:3])[:-1] + ', ... , ' + str(bcis_arr[-3:])[1:]

        f.write(f'Test data: {k} ({arr_preview})\n')

        # Run BCIS
        f.write('(BCIS) Sorting...\n')

        # Calculate runtime & memory usage
        start_time = time.perf_counter()

        bcis.sort(bcis_arr)  # sorts in-place

        end_time = time.perf_counter()

        f.write(f'(BCIS) Sorted ->  {comparator == bcis_arr}\n')
        bcis_elapsed = (end_time - start_time) * 1000  # to ms

        # Run Counting Sort
        f.write('(Counting Sort) Sorting... \n')

        start_time = time.perf_counter()

        cs_arr = counting_sort.sort(arr)  # not in-place

        end_time = time.perf_counter()

        f.write(f'(Counting Sort) Sorted -> {comparator == cs_arr}\n')
        cs_elapsed = (end_time - start_time) * 1000  # to ms

        f.write(f'BCIS Runtime: {bcis_elapsed:.2f} ms.\n')
        f.write(f'CS Runtime: {cs_elapsed:.2f} ms.\n')
        f.write('Done.\n\n')
        print(' done.')

    print(
        '''
        Done.
        Results exported to output.txt.
        ''')
    
    f.close()
