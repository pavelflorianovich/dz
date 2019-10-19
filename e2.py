def sel_sort(array):
    for i, e in enumerate(array):
        mn = min(range(i, len(array)), key=array.__getitem__)
        array[i], array[mn] = array[mn], e
    return array
