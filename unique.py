def uniqueElements(lst):
    result = []
    seen = []
    for item in lst:
        if not any(item == x and type(item) == type(x) for x in seen):
            seen.append(item)
            result.append(item)
    return result