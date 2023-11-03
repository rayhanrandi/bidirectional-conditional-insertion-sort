class BCIS:
    def sort(self, arr: list[int]) -> None:
        """
        Bidirectional-Conditional-Insertion-Sort implementation -> O() time
        """
        # TODO: implement BCIS algorithm
        SL = 0
        SR = len(arr) - 1

        while SL < SR:
            mid = (SR - SL) / 2
            self.swap(arr, SR, SL + mid)

            if arr[SL] == arr[SR]:
                if self.is_equal(arr, SL, SR) == -1:
                    return
                
            if arr[SL] > arr[SR]:
                self.swap(arr, SL, SR)

            if (SR - SL) >= 100:
                for i in range(SL + 1, pow((SR - SL), 0.5)):
                    if arr[SR] < arr[i]:
                        self.swap(arr, SR, i)
                    elif arr[SL] > arr[i]:
                        self.swap(arr, SL, i)

            else:
                i = SL + 1

            LC = arr[SL]
            RC = arr[SR]

            while i < SR:
                curr_item = arr[i]

                if curr_item >= RC:
                    arr[i] = arr[SR - 1]
                    self.ins_right(arr, curr_item, SR, arr[len(arr) - 1])
                    SR -= 1

                elif curr_item <= LC:
                    arr[i] = arr[SL + 1]
                    self.ins_left(arr, curr_item, SL, arr[len(arr) - 1])
                    SL += 1
                    i += 1
                    
                else:
                    i += 1
            
            SL += 1
            SR -= 1

    # Helper functions
    def is_equal(self, arr: list[int], SL: int, SR: int) -> int:
        """
        
        """
        for k in range(SL + 1, SR - 1):
            if arr[k] != arr[SL]:
                self.swap(arr, k, SL)
                return k
        return -1
    
    def ins_right(self, arr: list[int], curr_item: int, SR: int, right: int) -> None:
        """
        
        """
        j = SR
        while j <= right and curr_item > arr[j]:
            arr[j - 1] = arr[j]
            j += 1
        arr[j - 1] = curr_item

    def ins_left(self, arr: list[int], curr_item: int, SL: int, left: int) -> None:
        """
        
        """
        j = SL
        while j >= left and curr_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_item

    def swap(self, arr: list[int], i: int, j: int) -> None:
        """
        swap position of elements in array[i] and array[j]
        """
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


class CountingSort:
    def sort(self, arr: list[int]) -> list[int]:
        """
        Counting sort implementation -> O(n) time
        credits: https://stackabuse.com/counting-sort-in-python/
        """
        # Find the maximum element in the inputArray [O(n)]
        max_element = max(arr)

        count_array_length = max_element + 1

        # Initialize the count_array with (max+1) zeros [O(1)]
        count_array = [0] * count_array_length

        # Step 1 -> Traverse the arr and increase 
        # the corresponding count for every element by 1 [O(n)]
        for el in arr: 
            count_array[el] += 1

        # Step 2 -> For each element in the count_array, 
        # sum up its value with the value of the previous 
        # element, and then store that value 
        # as the value of the current element [O(k)]
        for i in range(1, count_array_length):
            count_array[i] += count_array[i-1] 

        # Step 3 -> Calculate element position
        # based on the count_array values [O(n)]
        output_arr = [0] * len(arr)
        i = len(arr) - 1
        while i >= 0:
            current_el = arr[i]
            count_array[current_el] -= 1
            new_position = count_array[current_el]
            output_arr[new_position] = current_el
            i -= 1

        return output_arr

