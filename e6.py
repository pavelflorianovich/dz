def sp(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1.difference(set2)
    return set3
