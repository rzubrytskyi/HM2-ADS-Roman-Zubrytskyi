import random

def random_array(size, lower_bound=-1000, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def find_duplicates(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    result = []
    i = 0
    while i < n:
        current = arr_sorted[i]
        count = 1
        i += 1
        while i < n and arr_sorted[i] == current:
            count += 1
            i += 1
        if count > 1:
            result.append((current, count))
    return result

def big_test():
    arr = random_array(10000)
    unique_arr = list(set(arr))
    sample = random.sample(unique_arr, 10)
    arr = sample + unique_arr + sample
    assert find_duplicates(arr) == [(i, 3) for i in sorted(sample)], "Big test failed"
assert find_duplicates([1, 2, 3, 4, 2, 3, 4, 5, 6]) == [(2, 2), (3, 2), (4, 2)], "Test case 1 failed"
assert find_duplicates([1, 2, 3, 4, 5]) == [], "Test case 2 failed"
assert find_duplicates([1, 1, 1, 1, 1]) == [(1, 5)], "Test case 3 failed"
assert find_duplicates([1, 2, 3, 3, 3, 4, 4, 5, 19, 5, 20]) == [(3, 3), (4, 2), (5, 2)], "Test case 4 failed"
assert find_duplicates([1, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7]) == [(7, 3)], "Test case 5 failed"

big_test()
