n = int(input())
studs = map(int, input().split())

studs = list(studs)
new_st = []
wrong = []
while len(studs) != 0:
    for n, i in enumerate(studs, 1):
        # проверяю, находится ли на первом месте нечетное число
        if n % 2 == 1 and i % 2 == 1:
            if n + 1 <= len(studs):
                # проверяю, находится ли на втором месте (если оно есть) четное число
                if (n + 1) % 2 == 0 and studs[(studs.index(i)) + 1] % 2 == 0:
                    new_st = new_st + studs[:2]
                    del studs[:2]
                    break  # если все цифры подходят условиям,
                    # то исходный список учеников после цикла становится пустым
                    # а новый список может теперь состоять из одного или более элементов
                else:
                    wrong = wrong + studs[1:2]  # wrong - список элементов, стоящих не на своих позициях
                    del studs[:2]
                    break
            else:
                new_st = new_st + studs[:1]
                del studs[:1]
                break


        else:
            wrong = wrong + studs[:1]
            if n + 1 <= len(studs):
                if (n + 1) % 2 == 0 and studs[(studs.index(i)) + 1] % 2 == 0:
                    del studs[:2]
                    break
                else:
                    wrong = wrong + studs[1:2]
                    del studs[:2]
                    break
            else:
                del studs[:1]
                break

# для проверки получившихся списков:
# print(studs)
# print(new_st)
# print(wrong)


if len(wrong) == 1 or len(wrong) > 2:
    print('-1 -1')

elif len(wrong) == 2:
    print(wrong[1], wrong[0], sep=' ')


elif len(studs) == 0:
    if len(new_st) > 2:
        print(new_st[2], new_st[0], sep=' ')
    else:
        print('-1 -1')
