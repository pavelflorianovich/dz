list1 = []


def mogno(dct, maxi):
    for key in dct:
        if dct[key] <= maxi:
            list1.append(key)
    return list1


mogno({'banana': 10, 'apple': 500, 'dog': 34, 'steak': 100}, 5)
