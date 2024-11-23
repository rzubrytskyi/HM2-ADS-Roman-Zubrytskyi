## Task 1 ##
def check_sorted(arr):
    non_ascending = True
    non_descending = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            non_ascending = False
        if arr[i] < arr[i - 1]:
            non_descending = False
    if non_ascending and non_descending:
        return 2
    elif non_descending:
        return 1
    elif non_ascending:
        return -1
    else:
        return 0

def check_sorted_tests():
    print("#1. Starting test cases for check_sorted")
    assert check_sorted([1, 2, 3, 4, 5]) == 1, "Test case 1 failed"
    assert check_sorted([5, 4, 3, 2, 1]) == -1, "Test case 2 failed"
    assert check_sorted([1, 2, 3, 5, 4]) == 0, "Test case 3 failed"
    assert check_sorted([1, 1, 1, 1, 1]) == 2, "Test case 4 failed"
    assert check_sorted([1, 2, 3, 3, 3, 4, 4, 5, 19, 5, 20]) == 0, "Test case 5 failed"
    print("\033[92mAll test cases passed\033[0m")

# Tasks 1.
check_sorted_tests()
