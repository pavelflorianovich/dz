def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


sel_sort([4, 76, 34, 64, 2, 8, 0, 354, 7, 2, 5])
