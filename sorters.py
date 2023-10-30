class BCIS:
    def sort(self, arr: list[int]) -> list[int]:
        """
        Bidirectional-Conditional-Insertion-Sort implementation -> O() time
        """
        # TODO: implement BCIS algorithm
        return []


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
        # as the value of the current element [O(n)]
        for i in range(1, count_array_length):
            count_array[i] += count_array[i-1] 

        # Step 3 -> Calculate element position
        # based on the count_array values [O(?)]
        output_arr = [0] * len(arr)
        i = len(arr) - 1
        while i >= 0:
            current_el = arr[i]
            count_array[current_el] -= 1
            new_position = count_array[current_el]
            output_arr[new_position] = current_el
            i -= 1

        return output_arr

