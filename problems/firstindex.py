def find_index(hs: str, ne: str) -> int:
    index = -1
    if hs.__contains__(ne):
        return hs.index(ne)
    else:
        return index


haystack = input().strip()
needle = input().strip()
print(find_index(haystack, needle))
