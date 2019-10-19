def mogno(dct, maxi):
    list1 = []
    for key in dct:
        if dct[key] <= maxi:
            list1.append(key)
    return list1


