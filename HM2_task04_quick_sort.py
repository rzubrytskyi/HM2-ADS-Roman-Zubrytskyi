import random

def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def quick_sort_abs(arr):
    def quick_sort_recursive(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        else:
            pivot = sub_arr[len(sub_arr) // 2]
            less = [x for x in sub_arr if abs(x) < abs(pivot)]
            equal = [x for x in sub_arr if abs(x) == abs(pivot)]
            greater = [x for x in sub_arr if abs(x) > abs(pivot)]
            return quick_sort_recursive(less) + equal + quick_sort_recursive(greater)
    sorted_arr = quick_sort_recursive(arr)
    arr[:] = sorted_arr

def basic_test(sorting_func):
    arr = [5, 4, 3, 2, 1]
    sorting_func(arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
    print("\033[92mBasic test passed\033[0m")

def random_test(sorting_func):
    arr = random_array(5)
    print("Random array: ", arr)
    sorting_func(arr)
    print("Sorted array: ", arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
    print("\033[92mRandom test passed\033[0m")

def medium_test(sorting_func):
    arr = random_array(500)
    sorting_func(arr)
    res = sorted(arr, key=abs)
    assert arr == res, f"Expected {res}, but my sort got {arr}"
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
    arr_copy.sort(key=abs)
    end = time.time()
    print(f"Time to sort 10,000 elements with built-in sort: {end - start:.6f} seconds")

    assert arr == arr_copy, f"Expected {arr_copy}, but my sort got {arr}"
    print("\033[92mBig test passed\033[0m")

if __name__ == "__main__":
    sorting_func = quick_sort_abs
    basic_test(sorting_func)
    random_test(sorting_func)
    medium_test(sorting_func)
    big_test(sorting_func)