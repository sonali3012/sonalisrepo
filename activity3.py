# Sonali's repo: https://github.com/sonali3012/sonalisrepo.git
# Aydin's repo: https://github.com/NupNupp/lunch.git
# Asim's repo: https://github.com/AsimMairaj/Asim-Repository

import random
import time

# Phase 1: Data Generation and Initial Sorting (Insertion Sort)
"""This function uses insertion sort to sort random numbers and the ones given in the word doc"""

def generate_sorted_data(size):  
    """This generates random integers and sorts them using insertion sort"""  
    data = [random.randint(1, 100) for _ in range(size)] #this makes the random array 

    for i in range(1, len(data)):  #insertion sort starts here 
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    return data  # Return the sorted random data

def insertion_sort(data):   #this is the function for the array given in the doc
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    return data  # Return the sorted list

# Phase 2: Implement Binary Search on Sorted Data
"""This function will take the sorted array above and implements binary search"""

def binary_search(sorted_array, target):
    left = 0  # Start of the search range
    right = len(sorted_array) - 1  # End of the search range

    while left <= right:
        mid = (left + right) // 2  #this finds the middle of the array

        if sorted_array[mid] == target:
            return mid  # Target found, return its index

        # If target is greater than mid element, search in the right half
        elif sorted_array[mid] < target:
            left = mid + 1

        # If target is smaller than mid element, search in the left half
        else:
            right = mid - 1

    return None

# Phase 3: Merge Sort Implementation
def merge_sort_split(array):
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]
    return left_array, right_array  

def merge_sort_merge(left_array, right_array):
    merged_array = []
    left_index = 0
    right_index = 0 

    while left_index < len(left_array) and right_index < len(right_array): 
        if left_array[left_index] <= right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])  
            right_index += 1

    if left_index < len(left_array):
        merged_array = merged_array + left_array[left_index:]
    else:
        merged_array = merged_array + right_array[right_index:]
        
    return merged_array

def merge_sort(array):
    if len(array) < 2:
        return array  
    else:
        left_array, right_array = merge_sort_split(array)
        sorted_left = merge_sort(left_array)  
        sorted_right = merge_sort(right_array)
        return merge_sort_merge(sorted_left, sorted_right)

# Phase 4: Search Performance Comparison
def linear_search(arr, target):
    """Performs linear search to find the target in an array and returns its index if found."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None

def main():
    """Phase 1"""
    print("Phase 1")
    random_data_sorted = generate_sorted_data(10)
    print("random data sorted is: ", random_data_sorted)

    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
    small_data_sorted = insertion_sort(small_data)
    print("small data sorted is: ", small_data_sorted)

    print("") 

    """Phase 2"""
    print("Phase 2")
    target_1 = int(input("Enter a value you want to be found: "))
    target_2 = 100
    print(f"Index of {target_1}:", binary_search(small_data_sorted, target_1))  # Expected index
    #print(f"Index of {target_2}:", binary_search(small_data_sorted, target_2))  # Expected result: None

    print("")

    """Phase 3"""
    print("Phase 3")
    test = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
    sorted_test = merge_sort(test)
    print("First 10 elements of sorted large data:", sorted_test[:10])

    print("")

    """Phase 4"""
    print("Phase 4")
    target = 72
    start_time = time.perf_counter()
    linear_index = linear_search(sorted_test, target)
    linear_search_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    binary_index = binary_search(sorted_test, target)
    binary_search_time = time.perf_counter() - start_time

    print("Linear Search Index:", linear_index)
    print("Linear Search Time:", linear_search_time, "seconds")
    print("Binary Search Index:", binary_index)
    print("Binary Search Time:", binary_search_time, "seconds")

main()
