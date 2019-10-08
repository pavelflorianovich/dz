list1 = []
x = 2
while x < 1001:
    i = 2
    while x % i != 0:
        i += 1
    if i == x:
        list1.append(x)
    x += 1
print(list1)
