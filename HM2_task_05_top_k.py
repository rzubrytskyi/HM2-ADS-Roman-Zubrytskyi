def top_k_frequent_elements(arr, k):
    max_value = 1000
    freq = [0] * (max_value + 1)
    for num in arr:
        freq[num] += 1
    n = len(arr)
    frequency = [[] for _ in range(n + 1)]
    for num in range(1, max_value + 1):
        f = freq[num]
        if f > 0:
            frequency[f].append(num)
    result = []
    for i in range(n, 0, -1):
        if frequency[i]:
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
    return result

# Testing function
def test_top_k_frequent_elements():
    test_cases = [
        # Format: (input_array, k, expected_output)
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 6], 3, [2, 3, 4]),
        ([5, 5, 5, 4, 4, 3, 3, 3, 3], 2, [3, 5]),
        ([1000] * 1000 + [999] * 999 + [998] * 998, 2, [1000, 999]),
        # Smallest Input
        ([1], 1, [1]),

        # All Elements with the Same Frequency
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),

        # All Elements Are the Same
        ([1, 1, 1, 1], 1, [1]),

        # Duplicate Frequencies
        ([1, 1, 2, 2, 3, 3, 4, 5], 3, [1, 2, 3]),

        # Array Larger than the Range of Values
        ([1, 2, 3] * 333 + [4], 3, [1, 2, 3]),

        # k Larger than the Number of Unique Elements
        ([1, 1, 2], 5, [1, 2]),

        # Array with Extreme Values
        ([1, 1000, 1, 1000, 1, 500], 2, [1, 1000]),

        # Large Array with Uneven Frequencies
        ([5] * 1000 + [4] * 500 + [3] * 300 + [2] * 200 + [1], 4, [5, 4, 3, 2]),

        # k Equals Total Number of Unique Elements
        ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),

        # Unsorted Array with Large k
        ([2, 3, 1, 2, 3, 4, 3, 1, 4, 5, 6, 7, 8, 9, 10, 3], 4, [3, 2, 1, 4]),

        # Array with Gaps in the Range
        ([10, 20, 30, 10, 20, 40, 50, 10], 2, [10, 20]),

        # Maximal Edge Case
        ([1] * 1000 + [2] * 999 + [3] * 998, 3, [1, 2, 3]),
    ]

    for idx, (arr, k, expected) in enumerate(test_cases, start=1):
        result = top_k_frequent_elements(arr, k)
        print(f"\033[94mTest Case {idx}:\033[0m")
        print(f"\033[93mInput: arr={arr[:10]}{'...' if len(arr) > 10 else ''}, k={k}\033[0m")
        print(f"\033[92mExpected: {expected}\033[0m")
        print(f"\033[96mResult: {result}\033[0m")
        if set(result) == set(expected):
            print(f"\033[92mPass: {set(result) == set(expected)}\033[0m\n")
        else:
            print(f"\033[91mPass: {set(result) == set(expected)}\033[0m\n")
            assert False, "Test #{} failed".format(idx)

test_top_k_frequent_elements()
