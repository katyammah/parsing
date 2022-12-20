n, k = map(int, input().split())
m = map(int, input().split())

mas = list(m)
sum1 = sum(mas)
mas = list(map(lambda x: str(x).zfill(len(str(max(mas)))), mas))
mas.sort()

digit = 0
while True:
    try:
        mas.sort(key=lambda x: x[digit])
        for n, item in enumerate(mas):
            if k == 0:
                break

            if set(item[:digit + 1]) != {'0'} and item[digit] != '9':
                change = list(item)
                change[digit] = '9'
                mas[n] = ''.join(change)
                k -= 1

        else:
            digit += 1
            continue
        break

    except IndexError:
        break

mas2 = list(map(int, mas))
sum2 = sum(mas2)
dif = sum2 - sum1

print(dif)
