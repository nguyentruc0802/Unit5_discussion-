"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Iterate through every index and element in the list from start to end
    for index in range(len(lst)):
        # Check if the current element matches the target
        if lst[index] == target:
            return index  # Target found, return its index immediately

    # Linear search has O(n) time complexity because, in the worst-case scenario,
    # the algorithm must inspect every single element (n) one by one.
    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Initialize pointers for the start and end of the current search space
    low = 0
    high = len(lst) - 1

    # Continue searching as long as the search space is valid
    while low <= high:
        # Find the middle index of the current search space
        mid = (low + high) // 2

        # Check if the middle element is the target
        if lst[mid] == target:
            return mid

        # list is sorted, comparing the target to the middle element allows
        # us to eliminate half of the remaining elements in each step.
        elif lst[mid] < target:
            # Target must be in the upper half; discard the left half including mid
            low = mid + 1
        else:
            # Target must be in the lower half; discard the right half including mid
            high = mid - 1

    # Return -1 if the search space becomes empty without finding the target
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_data = [4, 11, 18, 25, 33, 42, 57, 64, 79, 90]
    existing_target = 42
    missing_target = 50

    # Test searching for an existing value
    lin_found = linear_search(small_data, existing_target)
    bin_found = binary_search(small_data, existing_target)
    print(
        f"Searching for {existing_target} -> Linear Index: {lin_found}, Binary"
        f" Index: {bin_found}"
    )

    # Test searching for a non-existent value
    lin_missing = linear_search(small_data, missing_target)
    bin_missing = binary_search(small_data, missing_target)
    print(
        f"Searching for {missing_target} -> Linear Index: {lin_missing}, Binary"
        f" Index: {bin_missing}"
    )

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted list of 1,000 integers (0 to 999)
    large_data = list(range(1_000))
    # Pick a target near the very end to simulate a worst-case scenario
    large_target = 998

    # Measure Linear Search execution time
    start_time = time.perf_counter()
    lin_large_res = linear_search(large_data, large_target)
    lin_duration = time.perf_counter() - start_time

    # Measure Binary Search execution time
    start_time = time.perf_counter()
    bin_large_res = binary_search(large_data, large_target)
    bin_duration = time.perf_counter() - start_time

    print(
        f"Linear Search found {large_target} at index {lin_large_res} in"
        f" {lin_duration:.6f} seconds."
    )
    print(
        f"Binary Search found {large_target} at index {bin_large_res} in"
        f" {bin_duration:.6f} seconds."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    # Both algorithms safely avoid entering their loops (len is 0, low > high)
    # and immediately return -1 without throwing an IndexError.
    empty_list = []
    print(
        f"1. Empty List (target 10) -> Linear: {linear_search(empty_list, 10)},"
        f" Binary: {binary_search(empty_list, 10)}"
    )

    # Edge Case 2: Single-element list
    # Linear checks index 0. Binary sets low=0, high=0, mid=0, checks index 0,
    # and either returns 0 or adjusts pointers so low > high and exits.
    single_list = [99]
    print(
        "2a. Single-Element Found (target 99) -> Linear:"
        f" {linear_search(single_list, 99)}, Binary:"
        f" {binary_search(single_list, 99)}"
    )
    print(
        "2b. Single-Element Missing (target 5) -> Linear:"
        f" {linear_search(single_list, 5)}, Binary:"
        f" {binary_search(single_list, 5)}"
    )

    # Edge Case 3: Target at the first and last positions
    # Linear search is O(1) best-case for the first item, but O(n) worst-case
    # for the last item. Binary search takes O(log n) steps for both boundaries.
    boundary_list = [10, 20, 30, 40, 50]
    print(
        "3a. First Element (target 10) -> Linear:"
        f" {linear_search(boundary_list, 10)}, Binary:"
        f" {binary_search(boundary_list, 10)}"
    )
    print(
        "3b. Last Element (target 50) -> Linear:"
        f" {linear_search(boundary_list, 50)}, Binary:"
        f" {binary_search(boundary_list, 50)}"
    )


if __name__ == "__main__":
    main()
