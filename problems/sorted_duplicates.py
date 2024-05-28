def remove_duplicates_in_sorted_array(arr: list) -> int:
    return len(set(arr))


print(remove_duplicates_in_sorted_array([1, 1, 2, 2, 3, 3, 4, 4]))