l, r = map(int, input().split())

list1 = []
for i in range(l, r + 1):
    list1.append(str(i))

list2 = []
for i in list1:
    res = list(i)
    if len(set(res)) == 1:
        list2.append(i)

print(len(list2))
