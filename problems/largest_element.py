def largest_element(arr: list) -> int:
    """

    :rtype: int
    """
    large = -float('inf')
    for i in arr:
        if i > large:
            large = i
    return large


print(largest_element([1, 2, 3, 4, 5, 6, 7, 99]))
