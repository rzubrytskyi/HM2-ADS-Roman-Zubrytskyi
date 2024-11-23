import random

def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mBasic test passed\033[0m")

def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    sorting_func(arr)
    print("Sorted array: ", arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mRandom test passed\033[0m")

def medium_test(sorting_func):
    arr = random_array(500)
    sorting_func(arr)
    assert arr == sorted(arr), f"Expected {sorted(arr)}, but my sort got {arr}"
    print("\033[92mMedium test passed\033[0m")

def big_test(sorting_func):
    arr = random_array(10000)
    arr_copy = arr.copy()

    import time
    start = time.time()
    sorting_func(arr)
    end = time.time()
    print(f"Time to sort 10,000 elements: {end - start:.6f} seconds")

    start = time.time()
    arr_copy.sort()
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr == arr_copy, f"Expected {arr_copy}, but my sort got {arr}"
    print("\033[92mBig test passed\033[0m")

if __name__ == "__main__":
    sorting_func = merge_sort
    print("Merge sort")
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)

    sorting_func = insertion_sort
    print("\nInsertion sort")
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)
