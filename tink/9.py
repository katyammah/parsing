days = int(input())
pays = []
for i in range(days):
    a = int(input())
    pays.append(a)

sum1 = 0

while len(pays) != 0:
    for i in pays:
        if i > 100:
            meet = pays.index(i)
            sum1 += i
            del pays[:meet + 1]
            if len(pays) != 0:
                m = max(pays)
                pays.remove(m)
            break

        else:
            sum1 += i
            pays.remove(i)
            break

print(sum1)
